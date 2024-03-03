def lenf(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
print(lenf("input.txt"))
