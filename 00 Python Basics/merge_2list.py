def create_list(size):
    l = []
    for i in range(size):
        elem = int(input("Enter a number : "))
        l.append(elem)
    return l


size1 = int(input("Enter a size of list 1 : "))
l1 = create_list(size1)
size2 = int(input("Enter a size of list 2 : "))
l2 = create_list(size2)
print("list1 =", l1, "\nlist2 = ", l2)
l = l1 + l2
print("MergedList =", l, "\nSortedMergedList =", sorted(l))
