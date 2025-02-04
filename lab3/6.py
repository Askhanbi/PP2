# TASK 6    class
def PRIME(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

x = [int(i) for i in input().split()]
prove_prime = [PRIME(i) for i in x]
print(prove_prime)
