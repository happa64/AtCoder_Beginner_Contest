def CRT(B, M):
    """
    :param B: 余りのリスト
    :param M: modのリスト
    :return: x ≡ r (mod. m)の (r, m) を返す。解（周期）無しの場合、(0, -1)を返す
    """
    def extgcd(a, b):
        if b:
            d, y, x = extgcd(b, a % b)
            y -= (a // b) * x
            return d, x, y
        return a, 1, 0

    b1, m1 = 0, 1
    for b2, m2 in zip(B, M):
        d, p, q = extgcd(m1, m2)
        if (b2 - b1) % d != 0:
            return 0, -1
        tmp = (b2 - b1) // d * p % (m2 // d)
        b1 += m1 * tmp
        m1 *= m2 // d
    return b1 % m1, m1

# x ≡ 2(mod.3) && x≡3(mod.5) == x≡8(mod.15)
r, m = CRT([2, 3], [3, 5])  # 8, 15
