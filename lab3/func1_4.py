def filter_prime(list):
    for x in list:
        s = False
        for y in range(2, x):
            if x % y == 0:
                s = True
                break
        if s == False:
            print(x)
numbers = [2, 4, 5, 7, 9, 12, 17]
filter_prime(numbers)