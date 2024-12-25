def countingsort(A, n, k):
    B = [0]*(n)
    C = [0]*(k+1)
    for j in range(0, n):
        C[A[j]] = C[A[j]]+1
    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
    for j in range(n-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]]-1
    return B


while(True):
    x = int(input())
    if(x == 0):
        break
    y = list(map(int, input().split()))
    tmp = max(y)
    y = countingsort(y, x, tmp)
    for i in range(len(y)):
        print(y[i], end=" ")
    print("")
