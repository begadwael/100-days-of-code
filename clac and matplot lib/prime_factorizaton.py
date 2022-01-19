import math
from termcolor import colored
def primefactors(n):

    while n % 2  == 0:
        print(colored(2, 'cyan'), end=' ')
        n = n / 2
    
    for i in range(3,int(math.sqrt(n))+1,2):

        while (n % i == 0):
            print(colored(i, 'cyan'), end=' ')
            n = n / i

    if n > 2:
        print(n)

n = int(input("Enter the number for calculating it prime factors : "))
primefactors(n)