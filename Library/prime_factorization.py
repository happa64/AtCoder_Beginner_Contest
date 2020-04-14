# nを因数を返す
def prime_factorization(n):
    res = []
    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            ex = 0
            while n % i == 0:
                ex += 1
                n //= i
            res.append([i, ex])
    if n != 1:
        res.append([n, 1])

    prime = []
    for p in res:
        for _ in range(p[1]):
            prime.append(p[0])

    return prime
