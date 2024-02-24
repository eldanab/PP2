#Ex.5
def desc(N):
    for i in range(N, -1, -1):
        yield i
n = int(input())
x = desc(n)
print(*x)