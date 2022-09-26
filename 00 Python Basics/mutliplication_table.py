def mul_table(n):
    for i in range(1, 11):
        if i<10:
            print(n, "x", i, " =", n * i)
        else:
            print(n, "x", i, "=", n*i)


n = int(input("Enter your number : "))
mul_table(n)