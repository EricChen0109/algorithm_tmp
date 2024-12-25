def mergesort(A, p, r):
    if(p >= r):
        return
    q = int((p+r)//2)
    mergesort(A, p, q)
    mergesort(A, q+1, r)
    merge(A, p, q, r)


def merge(A, p, q, r):
    nl = q-p+1
    nr = r-q
    L = [0]*(nl)
    R = [0]*(nr)
    for i in range(nl):
        L[i] = A[p+i]
    for j in range(nr):
        R[j] = A[q+j+1]
    i = 0
    j = 0
    k = p
    while (i < nl and j < nr):
        if(L[i] <= R[j]):
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1
        k = k+1


amount = int(input())
A = list(map(int, input().split(' ')))
mergesort(A, 0, len(A)-1)
for i in range(len(A)):
    print(A[i], end=' ')
