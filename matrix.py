

def matrix(p, n):
    m = [[0]*n for i in range(n)]
    s = [[0]*n for i in range(n)]
    for i in range(0, n):
        m[i][i] = 0
    for l in range(2, n):
        for i in range(1, n-l+1):
            j = i+l-1
            m[i][j] = float('inf')

            for k in range(i, j):
                q = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m[1][n-1], s


def print_optimal_parens(s, i, j):
    if i == j:
        print('A', i, sep='', end=' ')
    else:
        print('(', end=' ')
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j]+1, j)
        print(')', end=' ')


y = list(map(int, input().split(" ")))
m, s = matrix(y, len(y))
print(int(m))
print_optimal_parens(s, 1, len(y)-1)
