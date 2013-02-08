primeFactor = 600851475143
counter = primeFactor - 1

def CheckPrime(numCheck):
    i = numCheck - 1
    while i >= 2:
        if numCheck % i == 0:
            return 0
        i -= 1
    return 1

while counter >= 2:
    if (primeFactor % counter == 0):
        if CheckPrime(counter):
            print counter
    counter -= 1

''' range() has a max
for i in range(2, primeFactor):
    if (primeFactor % i == 0):
        if CheckPrime(i):
            print i
''' 