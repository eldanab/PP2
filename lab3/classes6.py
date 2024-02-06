def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

list1 = [2, 3, 6 ,7, 8, 9, 11]
print(list(filter(lambda x : prime(x), list1)))