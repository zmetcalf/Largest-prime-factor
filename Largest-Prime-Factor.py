primeFactor = 600851475143
counter = 2

def CheckPrime(numCheck):
    i = 2
    while i < numCheck:
        if numCheck % i == 0:
            return 0
        i += 1
    return 1

while counter < primeFactor:
    if (primeFactor % counter == 0):
        if CheckPrime(counter):
            print counter
    counter += 1

''' range() has a max
for i in range(2, primeFactor):
    if (primeFactor % i == 0):
        if CheckPrime(i):
            print i
''' 