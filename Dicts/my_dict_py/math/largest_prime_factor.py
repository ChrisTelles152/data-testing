import math
def is_prime(num):
    for i in range(int(math.sqrt(num)),1,-1):
        if num % i == 0:
            print(i)
            return False
    return True
def largest_prime_factor(num):
    is_prime(num)
    for i in range(int(math.sqrt(num)), 1, -1):
        if num % i == 0 and is_prime == True:
            print(i + "hey")
            return i
    return None
largest_prime_factor(600851475143)
