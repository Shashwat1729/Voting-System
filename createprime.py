import random

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime(n_bits):
    while True:
        p = random.getrandbits(n_bits)
        if is_prime(p):
            return p

prime = generate_prime(32)
print(prime)
