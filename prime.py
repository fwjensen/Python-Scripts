def prime(n):
    for x in range(2,n):
        if n / x:
            break

num = input("What prime number do you want? ")

open('primes.txt','w+')
