# aとbの最大公約数を返す(ユークリッドの互除法）
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 受け取った配列の最大公約数の個数を返す
def ngcd(a):
    res = a[0]
    for i in range(len(a)):
        if res != 1:
            res = gcd(a[i], res)
    return res


# aとbの最小公倍数を返す
def lcm(a, b):
    return a * b // gcd(a, b)


# 受け取った配列の最小公倍数の個数を返す
def nlcm(a):
    res = a[0]
    for i in range(len(a)):
        res = lcm(res, a[i])
    return res
