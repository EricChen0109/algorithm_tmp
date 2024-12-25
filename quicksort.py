def partition(A, p, r):
    z = A[r]
    i = p-1
    for j in range(p, r):
        if (A[j] <= z):
            i = i+1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    tmp = A[r]
    A[r] = A[i+1]
    A[i+1] = tmp
    return i+1


def quicksort(A, p, r):
    if(p > r):
        return A
    q = partition(A, p, r)
    quicksort(A, p, q-1)
    quicksort(A, q+1, r)


while(True):
    x = int(input())
    if (x == 0):
        break
    y = list(map(int, input().split()))
    quicksort(y, 0, x-1)
    for i in range(len(y)):
        print(y[i], end=" ")
