# 二項係数(mod p)をO(1)で求める
def cmb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod


fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, n + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)


def cmb_mod(n, r, mod):
    x, y = 1, 1
    for i in range(r):
        x = (x * (n - i)) % mod
        y = (y * (i + 1)) % mod
    return (x * pow(y, mod - 2, mod)) % mod