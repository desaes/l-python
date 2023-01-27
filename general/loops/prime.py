"""
# prime numbers
for n in range(2,100000):
    for x in range(2,n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number.")
"""


# Python program to print all Primes Smaller 
# than or equal to N using Sieve of Eratosthenes
  
  
def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
# boolean array
    p = 2
    while (p * p <= num):
  
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
  
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
  
    # Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            print(p)
  
  
# Driver code
if __name__ == '__main__':
    num = 10000000
    print("Following are the prime numbers smaller"),
    print("than or equal to", num)
    SieveOfEratosthenes(num)