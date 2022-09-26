def reverse_number(n):
    rev = 0
    while n > 0:
        a = n % 10
        rev = rev*10 + a
        n = n//10
    return rev


n = int(input("Enter your number : "))
rev = reverse_number(n)

if n == rev:
    print(rev, "is a palindrome number")
else:
    print(n, "is not a palindrome number")
