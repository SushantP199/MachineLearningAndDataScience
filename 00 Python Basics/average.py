def average(n, l):
    sum = 0
    for elem in l:
        sum += elem
    avg = sum/n
    return avg


def list_creation(n):
    l =[]
    for i in range(n):
        l = l + [int(input("Enter a item : "))]
    return l


n = int(input("Enter number of elemnets you want in a list : "))
l = list_creation(n)
print("Average =", average(n, l))
