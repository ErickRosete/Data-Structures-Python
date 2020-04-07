class UndirectedGraph:
    def __init__(self, number_nodes):
        #self.adjList = [[]] * number_nodes   #Same reference
        self.adjList = [[] for _ in range(number_nodes)]
        self.number_nodes = number_nodes
        
    def addEdge(self, src, dest, cost = 1):
        if(not((dest, cost) in self.adjList[src])):
            self.adjList[src].append((dest, cost))
            self.adjList[dest].append((src, cost))
    
    def cycleSearch(self):
        discovered = [False] * self.number_nodes
        parents = [None] * self.number_nodes
        openList =[]
        
        #If graph is disconnected breadth first search in all subgraphs
        while(not(all(discovered))): 
            #Search a not discovered node
            node = next(i for i in range(self.number_nodes) if not(discovered[i]))
            discovered[node] = True
            openList.append(node)
            
            #Breadth first search
            while(len(openList) > 0):
                v = openList.pop(0)
                for next_v, _ in self.adjList[v]:
                    #print(v, " -> ", next_v)
                    #It was previously discovered 
                    if(discovered[next_v]):
                        #It it is not is parent 
                        if(parents[v] != next_v):
                            return True
                    else:
                        discovered[next_v] = True
                        parents[next_v] = v
                        openList.append(next_v)
        return False
    
    def depthFirstSearch(self, src, dest):
        visited = [False] * self.number_nodes
        visited[src] = True
        openList = [src]
        parents = [None] * self.number_nodes
        
        found = False
        while(not found and len(openList) > 0):
            v = openList.pop()
            if(v == dest):
                found = True
            else: 
                for next_v, cost in self.adjList[v]:
                    #print(v, " -> ", next_v)
                    if(not(visited[next_v])):
                        openList.append(next_v)
                        parents[next_v] = v
                        visited[next_v] = True
        
        if(found):
            print("Path found")
            path = []
            cur = v
            while(cur != None):
                path.append(cur)
                cur = parents[cur]
            path.reverse()
            print(" -> ".join(str(v) for v in path))
        else:
            print("Path not found")
        return found
        
    def breadFirstSearch(self, src, dest):
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
                    #print(v, " -> ", next_v)
                    #Explore only if it hasn't been explored before
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

    def cyclePrint(self):
        discovered = [False] * self.number_nodes
        parents = [None] * self.number_nodes
        openList =[]
        
        cycleFound = False
        #If graph is disconnected breadth first search in all subgraphs
        while(not cycleFound and not(all(discovered))): 
            #Search a not discovered node
            node = next(i for i in range(self.number_nodes) if not(discovered[i]))
            discovered[node] = True
            openList.append(node)
            
            #Breadth first search
            while(not cycleFound and len(openList) > 0):
                v = openList.pop(0)
                for next_v, _ in self.adjList[v]:
                    #print(v, " -> ", next_v)
                    #It was previously discovered 
                    if(discovered[next_v]):
                        #It it is not is parent 
                        if(parents[v] != next_v):
                            cycleFound = True
                            break
                    else:
                        discovered[next_v] = True
                        parents[next_v] = v
                        openList.append(next_v)
        
        #Cycle printing
        if(cycleFound):
            print("Cycle Found")
            #cycle root <-> ... <-> v <-> next_v <-> ... <-> root
            cycle = []
            
            #root <-> ... <-> v 
            cur = v
            while(cur != None):
                cycle.append(cur)
                cur = parents[cur]
            cycle.reverse()
            
            #next-v <-> ... <-> root 
            cur = next_v
            while(cur != None):
                cycle.append(cur)
                cur = parents[cur]
            
            #Look for inner cycle
            n = len(cycle)
            i = 0
            while(i < n - (i+1) and cycle[i] == cycle[-(i+1)]):
                i += 1
            minCycle = cycle[i-1: n-i+1]
            print(" -> ".join(str(v) for v in minCycle))
        else:
            print("Cycle not found")

    def print(self):
        for i in range(len(self.adjList)):
            print("Adjacency List of vertex ", i)
            print("head ->", end=" ")
            print(" -> ".join(str(v) for v in self.adjList[i]))

graph = UndirectedGraph(8)
graph.addEdge(0, 1) 
graph.addEdge(0, 2) 
graph.addEdge(0, 3) 
graph.addEdge(0, 4)
graph.addEdge(3, 7) 
graph.addEdge(5, 6) 
graph.addEdge(6, 7) 
graph.addEdge(7, 5) 

#graph.print()
graph.breadFirstSearch(2, 5)
graph.depthFirstSearch(2, 6)

print("Is there a cycle? ", graph.cycleSearch())
graph.cyclePrint()