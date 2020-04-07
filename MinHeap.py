# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:50:35 2020

@author: erick
"""

class MinHeap():
    def __init__(self):
        self.heap = []
        self.valueToPointer = {}
    
    def size(self):
        return len(self.heap)
    
    def insert(self, entry):
        self.heap.append(entry)
        entryPos = len(self.heap)-1
        self.valueToPointer[entry.value] = entryPos
        return self.upHeap(entryPos)
        
    def upHeap(self, p):
        #Invalid pointer
        if p >= len(self.heap) or p < 0:
            return False
        
        #Base case (root)
        if(p == 0):
            return True
        
        #Recursive routine
        par = (p - 1)//2
        if(self.heap[p].key < self.heap[par].key):
            self.swap(p, par)
            return self.upHeap(par)
        return True
        
    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]
        self.valueToPointer[self.heap[idx1].value] = idx1
        self.valueToPointer[self.heap[idx2].value] = idx2
        
    def deleteMin(self):
        if(len(self.heap) > 0):
            self.swap(0, len(self.heap)-1)
            minElement = self.heap.pop()
            del self.valueToPointer[minElement.value]
            self.downHeap(0)
            return minElement
        return None
    
    def downHeap(self, p):
        #Invalid pointer
        if p >= len(self.heap) or p < 0:
            return False
        
        #Base case (no children or only left child)
        lc = 2*p + 1
        rc = 2*p + 2
        if rc >= len(self.heap):
            if lc < len(self.heap) and self.heap[lc].key < self.heap[p].key:
                self.swap(lc, p)
            return True

        #Recursive routine (Both children)
        if(self.heap[p].key > self.heap[lc].key or self.heap[p].key > self.heap[rc].key):
            #Change lc to p
            if(self.heap[lc].key < self.heap[rc].key):
                self.swap(lc, p)
                return self.downHeap(lc)
            #change rc to p
            else:
                self.swap(rc, p)
                return self.downHeap(rc)
        return True     
    
    def getPointer(self, value):
        return self.valueToPointer[value]
            
    def decreaseKey(self, p, k):
        #Invalid pointer
        if p >= len(self.heap) or p < 0:
            print("Invalid")
            return False
        
        #k is smaller than stored key
        if(k < self.heap[p].key):
            self.heap[p].key = k
            return self.upHeap(p)
        return True
    
    def print(self):
        for heapEntry in self.heap:
            print("[", heapEntry.key, heapEntry.value, "]", end=' ')
        print()

class HeapEntry():
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
# minHeap = MinHeap()
# minHeap.insert(HeapEntry(10, "A"))
# minHeap.insert(HeapEntry(4, "B"))
# minHeap.insert(HeapEntry(3, "C"))
# minHeap.insert(HeapEntry(12, "D"))
# minHeap.insert(HeapEntry(8, "E"))
# minHeap.insert(HeapEntry(6, "F"))
# minHeap.insert(HeapEntry(2, "G"))
# minHeap.print()
# minEntry = minHeap.deleteMin()
# print(minEntry.key, minEntry.value)
# minHeap.print()
# minHeap.decreaseKey(4, 1)
# minHeap.print()
# print(minHeap.getPointer("B"))
# input("Press Enter to continue...")


