def create_list(size):
    l = []
    for i in range(size):
        elem = int(input("Enter a number : "))
        l.append(elem)
    return l


size = int(input("Enter the list size : "))
l = create_list(size)
l.sort(reverse=True)
print(f"Second largest element is ", l[1])
