def unique(list1):
    list2 = []
    for i in list1:
        if not(i in list2):
            list2.append(i)
    print(list2)
a = ["apple", "orange", "kiwi", "banana", "kiwi", "apple", "kiwi"]
unique(a)