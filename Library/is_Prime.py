# nが素数か判定する
def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(pow(n, 0.5)) + 1):
        if n % k == 0:
            return False
    return True

print(is_prime(1000033))
