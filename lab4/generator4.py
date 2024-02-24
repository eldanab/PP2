#Ex.4
def squares(A, B):
    for i in range(A, B+1):
        yield i ** 2

a = int(input())
b = int(input())
x = squares(a, b)
for i in x:
    print(i)