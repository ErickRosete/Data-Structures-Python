# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 23:02:05 2020

@author: erick
"""
from DirectedGraph import DirectedGraph


graph = DirectedGraph(8)
graph.addEdge(0, 1, 1) 
graph.addEdge(1, 2, 4)
graph.addEdge(1, 3, 3)
graph.addEdge(2, 3, 3)
graph.addEdge(2, 4, 2)
graph.addEdge(2, 5, 5)
graph.addEdge(4, 5, 2)
graph.addEdge(4, 6, 6)
graph.addEdge(5, 6, 1)

graph.addEdge(7, 0, 2)
graph.addEdge(7, 1, 4)
graph.addEdge(7, 3, 8)

distances = graph.altDijkstra(7)
for i in range(len(distances)):
    print("node:", i, "distance", distances[i])
