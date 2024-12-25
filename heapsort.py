def buildmaxheap(A, n, heapsize):
    for i in range(int(n/2), -1, -1):
        maxheapify(A, i, heapsize)


def maxheapify(A, i, heapsize):
    l = i*2+1
    r = i*2+2
    if(l <= heapsize and A[l] > A[i]):
        largest = l
    else:
        largest = i
    if(r <= heapsize and A[r] > A[largest]):
        largest = r
    if (largest != i):
        tmp = A[i]
        A[i] = A[largest]
        A[largest] = tmp
        maxheapify(A, largest, heapsize)


def heapsort(A, n, heapsize):
    buildmaxheap(A, n, n)
    for i in range(n, 0, -1):
        tmp = A[0]
        A[0] = A[i]
        A[i] = tmp
        heapsize = heapsize-1
        maxheapify(A, 0, heapsize)


x = int(input())-1
y = list(map(int, input().split(" ")))
heapsort(y, x, x)
for i in range(len(y)):
    print(y[i], end=' ')
