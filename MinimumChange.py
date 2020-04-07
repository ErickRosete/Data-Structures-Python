# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 21:45:10 2020

@author: erick
"""
memory = {}
def topDownMinimumChange(denominations, n):
    if(n in memory):
        return memory[n]
    if(n == 0):
        memory[n] = 0
        return memory[n]
    
    bestN = float('inf')
    for c in denominations:
        if(n - c >= 0):
            newN = 1 + topDownMinimumChange(denominations, n - c)
            if(newN < bestN):
                bestN = newN
                
    memory[n] = bestN
    return memory[n]

def bottomUpMinimumChange(denominations, n):
    numberCoins = [float('inf') for i in range(n+1)]
    numberCoins[0] = 0
    
    for i in range(n):
        for c in denominations:
            reachedValue = i + c
            if reachedValue <= n:
                cand = numberCoins[i] + 1
                if cand < numberCoins[reachedValue]:
                    numberCoins[reachedValue] = cand
                
    return numberCoins[n]
            
            
print(topDownMinimumChange([2,29,4,6], 100))
print(bottomUpMinimumChange([2,29,4,6], 100))