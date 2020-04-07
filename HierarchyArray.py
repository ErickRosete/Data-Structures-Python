import numpy as np

class HierarchyArray:
    def __init__(self):
        self.count = 0
        self.arrays = []
        
    def printArrays(self):
        for i in range(len(self.arrays)):
            print(self.arrays[i])
            
    def merge(self, arr1, arr2):
        n = len(arr1) + len(arr2)
        i = 0
        j = 0
        newArr = []
        for k in range(n):
            if  j >= len(arr2) or \
                i < len(arr1) and arr1[i] < arr2[j]:
                newArr.append(arr1[i])
                i += 1
            else:
                newArr.append(arr2[j])
                j += 1
        return newArr

    def insert(self, element):
        numberArrays = len(self.arrays)
        maxElements = 2**(numberArrays) - 1
        
        if(self.count+1 > maxElements):
            #Expand number of arrays
            auxArray = [element]
            for i in range(numberArrays):
                auxArray = self.merge(auxArray, self.arrays[i])
                self.arrays[i] = [None] * 2**i
            self.arrays.append(auxArray)
        else:
            #Normal Insert
            if (self.count + 1) % 2 == 1:
                self.arrays[0][0] = element
            else:
                auxArray = [element]
                for i in range(numberArrays):
                    if(self.arrays[i][0] is None): 
                        self.arrays[i] = auxArray
                        break
                    else:
                        auxArray = self.merge(auxArray, self.arrays[i])
                        self.arrays[i] = [None] * 2**i
        self.count += 1
    
    def search(self, k):
        for i in range(len(self.arrays)):
            if(self.arrays[i][0] is not None): 
                j = self.binarySearch(k, self.arrays[i], 0, len(self.arrays[i])-1)
                if(j):
                    return(i , j)
        return False

    def binarySearch(self, k, array, l, r):
        if( l >= r):
            if(array[l] == k):
                return l
            else:
                return False
            
        nby2 = int( (l + r)/2 )
        if(k == array[nby2]):
            return nby2
        else:
            if(k < array[nby2]):
                return self.binarySearch(k, array, l, nby2 - 1)
            else:
                return self.binarySearch(k, array, nby2 + 1, r)
       
        
hierArrays = HierarchyArray()
numbers = np.random.randint(50, 150)
for i in range(numbers):
    hierArrays.insert(np.random.randint(numbers))
hierArrays.printArrays()
searchFor = np.random.randint(numbers)
found = hierArrays.search(searchFor)
print(searchFor)
print(found)
