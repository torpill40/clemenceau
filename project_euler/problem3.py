# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5), 2):
        if n % i == 0:
            return False
    return True


n = 600851475143

for i in range(2, int(n ** 0.5)):
    if n % i == 0:
        print(i, "is prime:", is_prime(i))
