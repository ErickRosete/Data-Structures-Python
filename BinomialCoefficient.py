# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 20:52:11 2020

@author: erick
"""
memory = {}
def recBinomialCoefficient(n, k):
    state = (n,k)
    if(state in memory):
        return memory[state]
    
    if(k == 0 or k == n):
        memory[state] = 1
        return memory[state]
    
    memory[state] = recBinomialCoefficient(n-1, k) + recBinomialCoefficient(n-1, k-1)
    return memory[state]

recBinomialCoefficient(50,5)

def loopBinomialCoefficient(n, k):
    memory = [ [ 0 for j in range(k+1) ] for i in range(n+1) ] 
 
    for i in range(n+1):
        for j in range(k+1):
            if (j <= i):
                if(j == 0 or j == i):
                    memory[i][j] = 1
                else:
                    memory[i][j] = memory[i-1][j] + memory[i-1][j-1]
    
    return memory[n][k]
            
            
print(loopBinomialCoefficient(50, 5))