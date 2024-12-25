inf = 9999999
x = int(input())
y = int(input())
u = [0]*(y+1)
v = [0]*(y+1)
w = [0]*(y+1)
line = [0]*(x+1)


for i in range(0, x):
    line[i] = inf
line[0] = 0


for i in range(0, y):
    u[i], v[i], w[i] = map(int, input().split(" "))

for j in range(0, x-1):
    for k in range(0, y):
        if (line[v[k]] > line[u[k]] + w[k]):
            line[v[k]] = line[u[k]] + w[k]


t = 0
for i in range(0, y):
    if line[v[i]] > line[u[i]] + w[i]:
        t = 1
    if t == 1:
        print("Negative Cycle!")
        break

else:
    for i in range(0, x):
        print(float(line[i]), end=" ")
