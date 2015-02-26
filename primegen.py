def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return sieve
    
def gen_prime(l):
    print [2] + [i*2+1 for i, v in enumerate(sieve_for_primes_to(l)) if v and i>0]
    
    
gen_prime(10000000)
