"""
Contains 3 different approaches
"""

def find_primes_naive(n):
    """
    Naive Approach.
    Executing a loop upto the half of the number
    if it gets divisible, then break from the loop and
    don't append it to the primes list

    Time Complexity: O(n*n)
    """

    primes = list()

    for i in range(2,n):
        flag = True
        for j in range(i//2):
            if i%j==0:
                flag = False
                break
        if flag:
            primes.append(i)

    return primes

def find_primes_better(n):
    """
    Better Approach.
    This is based on the fact that
    one of the divisors must be less than or equal to the sqrt(N)
    So we check for divisibility only till sqrt(N)

    Time Complexity: O(N^3/2)
    """
    def isPrime(n):
        # corner case
        if n<1:
            return True
        if n<3:
            return True

        # so that we can skip by 5 in the below while loop
        if (n%2 == 0 or n%3 == 0):
            return False

        p = 5

        while p*p <=n:
            if n%p==0:
                return False

            p += 6

        return True

    primes = list()

    for i in range(2, n):
        if isPrime(i):
            primes.append(i)

    return primes

def find_primes_sieve_of_erathosthenes(n):
    """
    Best Approach.
    Sieve of Erathosthenes (read online)

    Time Complexity: O(N * loglog(N))
    """
    final = list()

    primes = [True]*(n+1)

    p = 2

    while p*p <= n:
        if primes[p]:

            for i in range(p*p, n+1, p):
                primes[i] = False

            p += 1

    for prime in primes:
        if prime:
            final.append(prime)

    return final

if __name__ == "__main__":
    n = int(input())

    print(find_primes_naive(n))
    print(find_primes_better(n))
    print(find_primes_sieve_of_erathosthenes(n))