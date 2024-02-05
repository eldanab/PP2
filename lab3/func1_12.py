def histogram(nums):
    for i in range(len(nums)):
        s = ""
        for j in range(nums[i]):
            s += "*"
        print(s)

n = [4, 9, 7]
histogram(n)
