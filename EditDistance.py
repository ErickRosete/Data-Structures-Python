# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:56:42 2020

@author: erick
"""
from collections import defaultdict

def bottomUpEditDistance(x, y):
    distance = defaultdict(lambda: float('inf'))
    cur_x, cur_y = "", ""
    distance[(cur_x, cur_y)] = 0
    
    for i in range(len(x)):
        for j in range(len(y)):
            state = (cur_x, cur_y)
            
            #delete
            del_state = (cur_x + x[i], cur_y)
            cand = distance[state] + 1
            if cand < distance[del_state]:
                distance[del_state] = cand
            
            #replace
            rep_state = (cur_x + x[i], cur_y + y[j])
            if(x[i] == y[j]):
                cand = distance[state]
            else:
                cand = distance[state] + 1
            if cand < distance[rep_state]:
                distance[rep_state] = cand
                
            #insert
            ins_state = (cur_x, cur_y + y[j])
            cand = distance[state] + 1
            if cand < distance[ins_state]:
                distance[ins_state] = cand
            
            cur_y = cur_y + y[j]
        cur_y = ""
            
        cur_x = cur_x + x[i]
    
    return distance[(x, y)]
    
memory = {}
def editDistance(x, y):
    state = (x, y)
    if state in memory:
        return memory[state]
    
    if len(x) == 0:
        memory[state] = len(y)
        return memory[state]
    if len(y) == 0:
        memory[state] = len(x)
        return memory[state]
    
    delete = 1 + editDistance(x[:-1], y)
    insert = 1 + editDistance(x, y[:-1]) 
    if(x[-1] == y[-1]):
        replace = editDistance(x[:-1], y[:-1])
    else:
        replace = 1 + editDistance(x[:-1], y[:-1])
    
    memory[state] = min(delete, insert, replace)
    return memory[state]
    
print(editDistance("ROSETEBEAS", "RODENT"))
print(bottomUpEditDistance("ROSETEBEAS", "RODENT"))