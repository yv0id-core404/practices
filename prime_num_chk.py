# Prime Number Checker
# Made by Yair Thura Linn

# Write your implementation below
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
is_prime(n)
print(is_prime(n))
