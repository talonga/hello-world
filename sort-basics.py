from datetime import datetime
import math
import random
import collections
import linkedlist
import que
import stak

fixedArr = [8, 5, 3, 1, 4, 0, 230, 909, 32, 15, -2, 99, 434, 2, 111]
minPoint = collections.namedtuple('min', ['a', 'i'])

def createRandArray(length, cap):
	arr = []
	for i in range(length):
		arr.append(math.floor(random.random() * cap))
	return arr

def createRandList(length, cap):
    list = linkedlist.LinkedList()
    for i in range(length):
        list.add(math.floor(random.random() * cap))
    return list
    
#O(nlogn)
def mergeSort(A, n):
    if n == 1: return A
    midpoint = math.floor(n/2)
    left = A[0:midpoint]
    right = A[midpoint:n]
    return merge(mergeSort(left, len(left)), mergeSort(right, len(right)))

def merge(A, B):
    if len(A) == 0 : return B
    if len(B) == 0 : return A
    if A[0] < B[0]:
        return [A[0]] + merge(A[1:len(A)], B)
    else:
        return [B[0]] + merge(A, B[1:len(B)])

#O(nlogn)
def quickSortList(A, low, high):
    if (low < high) :
        p = A.partition(low, high)
        quickSortList(A, low, p-1)
        quickSortList(A, p+1, high)
    return A

def quickSort(A, low, high):
    if (low < high) :
        p = partition(A, low, high)#market is in the right place
        quickSort(A, low, p-1)#sort the left, ignoring the marker
        quickSort(A, p+1, high)#sort the right, ignoring the marker
    return A

def partition(A, low, high):
    pivot = A[high]#use last element as a marker
    i = low-1
    for j in range(low, high):
        if A[j] < pivot:
            i += 1
            swap(A, i, j)#shuffle largerelement up to "j", while "i" retains the index of smaller elements
    swap(A, i+1, high)#slot the marker between smaller and larger
    return i+1

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]
    
#O(n^2)
def selectionSort(A):
    arr = list()
    for i in range(0, len(A)):
        b = findMin(A)
        arr.append(b.a)
        del A[b.i]
    return arr

def findMin(A):
    i = 0
    m = A[i]
    for j in range(1, len(A)):
        if A[j] < m:
            i = j
            m = A[i]
    return minPoint(m, i)
    
#list = createRandList(10, 2000)
#print(list)
#quickSortList(list, 1, list.length)
#print(list)
#arr = createRandArray(10,2000)
#print(arr)

tsStart = datetime.now();
s = stak.Stack()
s.push(1)
s.push(2)
s.push(21)
print(s)
print(s.pop())
print(s.pop())
print(s.pop())
print(s)
#sortedArr = quickSort(arr, 0, len(arr)-1)
#sortedArr = selectionSort(arr)
#sortedArr = mergeSort(arr, len(arr))
print(datetime.now() - tsStart);
#print(sortedArr)