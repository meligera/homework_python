list1 = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
list2 = [4, 5, 6, 6, 6, 4, 4]

def unique(list1):
    return list(set(list1))

def intersection_list(list1, list2):
    a = set(list1)
    b = set(list2)
    return set.intersection(a, b)

print(unique(list1))
print(intersection_list(list1, list2))
