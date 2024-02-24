import math
n = int(input())
l = int(input())
p = n * l
a = l / (2 * math.tan((math.pi)/n))
A = p * a /2
print(A)