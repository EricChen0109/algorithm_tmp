def insertionsort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while(i >= 0 and A[i] > key):
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A


count = input()
nums = list(map(int, input().split(' ')))
ans = insertionsort(nums)
for i in range(len(ans)):
    print(ans[i], end=' ')
