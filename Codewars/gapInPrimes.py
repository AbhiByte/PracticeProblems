def is_prime(a):
    return all(a % i for i in range(2, a))

def gap(g, m, n):
    for x in range(m, n+1):
        if is_prime(x) == True and is_prime(x+g) == True:
            return [x, x+g]
    return None
