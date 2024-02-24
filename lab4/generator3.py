#Ex.3
def gen_div(N):
    for i in range(N + 1):
            if i % 3 == 0 and i % 4 == 0:
                yield i

n = int(input())
x = gen_div(n)
print(*x)