def LCSlength(X, Y, m, n):
    b = [[0]*(n+1) for i in range(m+1)]
    c = [[0]*(n+1) for i in range(m+1)]
    for i in range(1, m):
        c[i][0] = 0
    for j in range(0, n):
        c[0][j] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if(X[i-1] == Y[j-1]):
                c[i][j] = c[i-1][j-1]+1
                b[i][j] = 4
            elif(c[i-1][j] >= c[i][j-1]):
                c[i][j] = c[i-1][j]
                b[i][j] = 5
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 1
    return c, b


def print_LCS(b, X, i, j):
    if(i == 0 or j == 0):
        return
    if(b[i][j] == 4):
        print_LCS(b, X, i-1, j-1)
        print(X[i-1], end="")
    elif(b[i][j] == 5):
        print_LCS(b, X, i-1, j)
    else:
        print_LCS(b, X, i, j-1)


x = list(input())
y = list(input())
c, b = LCSlength(x, y, len(x), len(y))
print_LCS(b, x, len(x), len(y))
