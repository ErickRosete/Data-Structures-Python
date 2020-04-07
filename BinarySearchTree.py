# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:42:36 2019

@author: erick
"""

class BinarySearchTreeNode():
    def __init__(self, value):
        self.value = value
        self.rightChild = None
        self.leftChild = None
        
class BinarySearchTree():
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if(self.root == None):
            self.root = BinarySearchTreeNode(value)
        else:
            current = self.root
            inserted = False
            while(not inserted):
                if(value > current.value):
                    if(current.rightChild != None):
                        current = current.rightChild
                    else:   
                        current.rightChild = BinarySearchTreeNode(value)
                        inserted = True
                elif(value < current.value):
                    if(current.leftChild != None):
                        current = current.leftChild
                    else:   
                        current.leftChild = BinarySearchTreeNode(value)
                        inserted = True
                else:
                    print("Repeated number")
                    break
                
    def findSuccessor(self, node):
        #Empty tree
        if(self.root == None):
            return None
        
        #Find value node
        successorParent = None
        current = self.root
        found = False
        while(not found):
            if(node.value == current.value):
                found = True
            elif(node.value < current.value):
                if(current.leftChild != None):
                    successorParent = current
                    current = current.leftChild
                else:
                    #Not existent value node
                    return None
            elif(node.value > current.value):
                if(current.rightChild != None):
                    current = current.rightChild
                else:
                    #Not existent value node
                    return None 
                
        #Look for successor value
        if(current.rightChild == None):
            if(successorParent != None):
                return successorParent
            else:
                #Max element in tree
                return None
        else:
            successor = current.rightChild
            while(successor.leftChild != None):
                successor = successor.leftChild
            return successor
        
    def print(self):
        if(self.root == None):
            print("Empty")
        else:
            currents = [self.root]
            while(len(currents) >= 1):
                nextCurrents = []
                for node in currents:
                    print(node.value, end = "  ")  
                    if(node.leftChild != None):
                        nextCurrents.append(node.leftChild)
                        print("", end = "  ")  
                    if(node.rightChild != None):
                        nextCurrents.append(node.rightChild)
                        print("", end = "  ")  
                print()
                currents = nextCurrents
        
bSTree = BinarySearchTree()
bSTree.print()
bSTree.insert(7)
bSTree.insert(5)
bSTree.insert(2)
bSTree.insert(1)
bSTree.insert(8)
bSTree.insert(3)
bSTree.insert(9)
bSTree.insert(4)
bSTree.print()

node = bSTree.root
print("Successor of", node.value)
print(bSTree.findSuccessor(node).value)

node = node.leftChild
print("Successor of", node.value)
print(bSTree.findSuccessor(node).value)

node = bSTree.root.rightChild
print("Successor of", node.value)
print(bSTree.findSuccessor(node).value)

node = BinarySearchTreeNode(3)
print("Successor of", node.value)
print(bSTree.findSuccessor(node).value)