import numpy as np

def binarySearch(k, array, l, r):
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
            return binarySearch(k, array, l, nby2 - 1)
        else:
            return binarySearch(k, array, nby2 + 1, r)
       
size = 21
array = np.random.randint(50, size=size)
array.sort()
print(array)
index = binarySearch(12, array, 0, size - 1)
print(index)