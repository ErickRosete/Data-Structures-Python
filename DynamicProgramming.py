# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:24:51 2020

@author: erick
"""

#!/bin/python3

import os
import heapq 
from collections import defaultdict

def valueIteration(prices):
    #Value iteration, reward = earned or lost money
    V = defaultdict(lambda: 0)
    delta = float('inf')
    while(delta > 0.5):
        openList = [(0, 0)] #price_idx, available
        delta = 0
        while len(openList)>0:
            state = openList.pop()
            price_idx, available = state
            v = V[state] 

            if(price_idx < len(prices)):
                next_state = (price_idx+1, available+1)
                buy = - prices[price_idx] + V[next_state]
                openList.append(next_state)

                next_state = (price_idx+1, available)
                nothing = V[next_state]
                openList.append(next_state)

                next_state = (price_idx+1, 0)
                sell = available * prices[price_idx] + V[next_state]
                openList.append(next_state)

                V[state] = max(buy, nothing, sell)
            delta = max(delta, abs(v - V[state]))
    return V[(0,0)]

def stockmax_loop(prices):
    V = defaultdict(lambda: 0)
    openList = []
    for i in range(len(prices)+1):
        heapq.heappush(openList, (-float('inf'), (len(prices), i)))

    while len(openList) > 0:
        _, state = heapq.heappop(openList)
        price_idx, available = state
        if(price_idx > 0):
            #buy
            next_state = (price_idx-1, available-1)
            cand = - prices[next_state[0]] + V[state]
            if cand > V[next_state]:
                V[next_state] = cand
                heapq.heappush(openList, (-V[next_state], (next_state)))

            #nothing
            next_state = (price_idx-1, available)
            cand = V[state]
            if cand > V[next_state]:
                V[next_state] = cand
                heapq.heappush(openList, (-V[next_state], (next_state)))

            #sell
            if(available == 0):
                for new_av in range(1, price_idx):
                    next_state = (price_idx-1, new_av)
                    cand = new_av*prices[next_state[0]] + V[state]
                    if cand > V[next_state]:
                        V[next_state] = cand
                        heapq.heappush(openList, (-V[next_state], (next_state)))
    return V[(0,0)]

def logicSolution(prices):
    maxPrice, acum = 0, 0
    for price in reversed(prices):
        if price < maxPrice:
            acum += maxPrice - price
        else:
            maxPrice = price
    return acum

def stockmax(prices):
    #return valueIteration(prices)
    #return stockmax_rec(prices, available = 0)
    #return stockmax_loop(prices)
    return logicSolution(prices)

memory = {}
def stockmax_rec(prices, available):
    if(len(prices) == 0):
        return 0

    state = (str(prices), available)
    if(state in memory):
        return memory[state]

    buy = stockmax_rec(prices[1:], available + 1) - prices[0]
    nothing = stockmax_rec(prices[1:], available)
    sell = stockmax_rec(prices[1:], 0) + available*prices[0]

    memory[state] = max(buy, nothing, sell)
    return memory[state]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
