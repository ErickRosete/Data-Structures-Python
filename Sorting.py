import numpy as np
import timeit

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def countingSort(arr):
    #map array to counts
    counts = [0] * (max(arr) + 1)
    for num in arr:
        counts[num] += 1
    
    #map counts to array in order
    ind = 0
    for i in range(len(counts)):
        for j in range(counts[i]):
            arr[ind] = i
            ind += 1
    return arr

#Time analysis
#Used to measure execution time of functions with arguments
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

sizes = (10, 100, 1000)
for size in sizes:
    bubbleArray = np.random.randint(1001, size=size)
    countArray = np.copy(bubbleArray)
    
    numberTest = round(10000/size)
    wrapped = wrapper(bubbleSort, bubbleArray)
    bubbleTime = timeit.timeit(wrapped, number=numberTest)
    bubbleTime = bubbleTime * 10**9 / numberTest
    print("Bubblesort - size: %d | time: %d ns" % (size, bubbleTime))
    
    wrapped = wrapper(countingSort, countArray)
    countTime = timeit.timeit(wrapped, number=numberTest)
    countTime = countTime * 10**9 / numberTest
    print("Countingsort - size: %d | time: %d ns" % (size, countTime))
