# nの約数を列挙列挙する
def make_divisors(n):
    divisors = []
    for i in range(1, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors
