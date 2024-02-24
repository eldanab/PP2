#Ex.1
def gen_sqr(N):
    for i in range(1, N+1):
        yield i ** 2

n = int(input())
x = gen_sqr(n)

for i in range(n):
    print(next(x))
