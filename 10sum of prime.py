import math
def isPrime(x):
    prime = True
    for i in range(2, round(math.sqrt(x))+1):
        if x % i == 0:
            prime = False
            break
        else:
            continue
    return prime

primes = (a for a in range(2, 2000000) if isPrime(a))
print(sum(primes))