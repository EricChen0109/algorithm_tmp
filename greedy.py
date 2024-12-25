def recursive_activity_selector(s, f, k, n):
    set0 = set()
    m = k+1
    while(m <= n and s[m] < f[k]):
        m = m+1
    if(m <= n):
        print(m, end=" ")
        return (recursive_activity_selector(s, f, m, n))
    else:
        return set0


def greedy_activity_selector(s, f, n):
    k = 0
    for m in range(1, n):
        if(s[m] >= f[k]):
            print(m, end=" ")
            k = m


x = list(map(str, input().split(" ")))
y = list(map(str, input().split(" ")))
if(x[len(x)-1] == ""):
    x.remove("")
x = list(map(int, x))
y = list(map(int, y))
recursive_activity_selector(x, y, 0, len(x)-1)
print("")
greedy_activity_selector(x, y, len(x))
