def isPrime(num):
    if num <=1: return False 
    for i in range (2,num):
        if num % i == 0:
            return False
    return  True

def returnPrime(list):
    primes = []
    for l in list:
        for p in l:
            if isPrime(p):
                primes += p
    return primes

