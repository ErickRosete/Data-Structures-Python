from MinHeap import MinHeap, HeapEntry

class DirectedGraph:
    def __init__(self, number_nodes):
        self.adjList = [[] for _ in range(number_nodes)]
        self.number_nodes = number_nodes
        
    def addEdge(self, src, dest, cost = 1):
        if(not((dest, cost) in self.adjList[src])):
            self.adjList[src].append((dest, cost))
            
    def reverseConnectedComponents(self, dest):
        #Create an aux reverse connected graph
        auxAdjList = [[] for _ in range(self.number_nodes)]
        for from_v in range(len(self.adjList)):
            for to_v, cost in self.adjList[from_v]:
                auxAdjList[to_v].append((from_v, cost))
       
        #Depth first search from destiny node
        openList=[dest]
        discovered = [False] * self.number_nodes
        discovered[dest] = True
        revConComps = []
        
        while len(openList)>0:
            v = openList.pop()
            for next_v, _ in auxAdjList[v]:
                if(not discovered[next_v]):
                    discovered[next_v] = True
                    openList.append(next_v)
                    revConComps.append(next_v)
        
        return revConComps
        
        
    def altRevConComps(self, dest):
        openList = [dest]
        #found path from node to dest
        foundPath = [False] * self.number_nodes
        foundPath[dest] = True
        revConComps = []
        
        while len(openList) > 0:
            open_v = openList.pop()
            for v in range(len(self.adjList)):
                if(not foundPath[v]):
                    for next_v, _ in self.adjList[v]:
                        if(next_v == open_v):
                            foundPath[v] = True
                            revConComps.append(v)
                            openList.append(v)
                            break
                        
        return revConComps
    
     
    def breadthFirstSearch(self, src, dest):
        discovered = [False] * self.number_nodes
        discovered[src] = True
        parents = [None] * self.number_nodes
        openList =[src]
        
        found = False 
        while(not found and len(openList) > 0):
            v = openList.pop(0)
            if(v == dest):
                found = True
            else:
                for next_v, _ in self.adjList[v]:
                    if(not discovered[next_v]):
                        discovered[next_v] = True
                        parents[next_v] = v
                        openList.append(next_v)
            
        if(found):
            print("Path found")
            cur = dest
            path = [cur]
            while(cur != src):
                cur = parents[cur]
                path.append(cur)
            path.reverse()
            print(" -> ".join(str(v) for v in path))
        else:
            print("Path Not Found")
        return found
    
    def dijkstra(self, src):
        visited = [False] * self.number_nodes
        distances = [float("inf")] * self.number_nodes
        distances[src] = 0

        #init heap
        priorityQueue = MinHeap()
        for i in range(len(distances)):
             priorityQueue.insert(HeapEntry(distances[i], i))
        
        while(priorityQueue.size() > 0):
            cur = priorityQueue.deleteMin()
            for to_v, cost in self.adjList[cur.value]:
                if(not visited[to_v]):
                    new_cost = cur.key + cost
                    p = priorityQueue.getPointer(to_v)
                    priorityQueue.decreaseKey(p, new_cost)  
            visited[cur.value] = True
            distances[cur.value] = cur.key
        return distances
    
    def altDijkstra(self, src):
        distances = [float("inf")] * self.number_nodes
        distances[src] = 0
        visited = [False] * self.number_nodes
        
        #init heap
        priorityQueue = MinHeap()
        priorityQueue.insert(HeapEntry(0, src))
        
        while(priorityQueue.size() > 0):
            cur = priorityQueue.deleteMin()
            if(not visited[cur.value]):
                visited[cur.value] = True
                for to_v, cost in self.adjList[cur.value]:
                    if(not visited[to_v]):
                        new_cost = distances[cur.value] + cost
                        if(new_cost < distances[to_v]):
                            priorityQueue.insert(HeapEntry(new_cost, to_v))
                            distances[to_v] = new_cost
        return distances
        
    def print(self):
        for i in range(len(self.adjList)):
            print("Adjacency List of vertex ", i)
            print("head ->", end=" ")
            print(" -> ".join(str(v) for v in self.adjList[i]))

# graph = DirectedGraph(8)
# graph.addEdge(0, 1) 
# graph.addEdge(0, 2) 
# graph.addEdge(0, 3) 
# graph.addEdge(0, 4)
# graph.addEdge(2, 3)
# graph.addEdge(3, 7) 
# graph.addEdge(5, 6) 
# graph.addEdge(6, 7) 
# graph.addEdge(7, 5) 

# #graph.print()
# graph.breadthFirstSearch(2, 5)
# print(graph.reverseConnectedComponents(7))
# print(graph.altRevConComps(7))

# input("Press Enter to continue...")
