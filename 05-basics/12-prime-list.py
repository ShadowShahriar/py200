from math import sqrt, floor


def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        for i in range(2, floor(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


nums = range(0, 1001)

print("")

primes = filter(isPrime, nums)
print(list(primes))

print("")

primesls = [n for n in range(0, 1001) if isPrime(n)]
print(primesls)
