import math

def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) +1 , 2):
        if n% i ==0:
            return False
    return True

def leftTrunc(x):
        #print(x)
        if(isPrime(int(x))):
            print(x)
            y=x
            count = 1
            while y>10:
                #print(y)
                y=y/10
                count = count + 1
            for z in range (1,10):
                if(isPrime(int(z*pow(10,count)+x))):
                    leftTrunc(int(z*pow(10,count)+x))

def rightTrunc(x):
        print(x)
        if(isPrime(int(x))):
            print(x)
            y=x
            count = 1
            while y>10:
                #print(y)
                y=y/10
                count = count + 1
            for z in range (1,10):
                if(isPrime(int(x*pow(10,count)+z))):
                    rightTrunc(int(x*pow(10,count)+z))

leftTrunc(3)