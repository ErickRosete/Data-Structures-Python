import numpy as np

def peakElement(array, l, r):
    if(l >= r):
        return l
    
    nby2 = int((l + r)/2)
    if(array[nby2] >= array[nby2 - 1] and array[nby2] >= array[nby2 + 1]):
        return nby2
    else:
        if(array[nby2] < array[nby2 -1]):
            return peakElement(array, l, nby2 - 1)
        else:
            return peakElement(array, nby2 + 1, r)

size = 21
array = np.random.randint(50, size=size)
index = peakElement(array, 0, size-1)
print(array)
if(index > 0 and index < 19):
    print(index)
    print(array[index-1:index+2])
else:
    if(index == 0):
        print(index)
        print(array[:2])
    else:
        print(index)
        print(array[-2:])
    