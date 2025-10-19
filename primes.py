
def isPrime(n, foundPrimes=None):
    foundPrimes = range(2, int(n**0.5)) if foundPrimes is None else foundPrimes
    for factor in foundPrimes:
        if n % factor == 0:
            return False
    return True

def listPrimes(max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n, foundPrimes):
            foundPrimes.append(n)
    return foundPrimes

print(f'primes.py module name is {__name__}')

# __name__ is a builtin python variable
# the line below says if __name__ is equal to __main__, that means this module is being
# called directly (ie: python3 primes.py), and the code in the if statement will execute
if __name__ == '__main__':
    print("this is a module, please import using primes")