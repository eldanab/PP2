#Ex.2
n = int(input())
def gen_even(N):
    for i in range(N+1):
        if i % 2 == 0:
            yield i

x = gen_even(n)
print(*x, sep = ", ")