def CRT(B, M):
    def extGcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = extGcd(b % a, a)
        return g, x - (b // a) * y, y

    b1, m1 = 0, 1
    for b2, m2 in zip(B, M):
        d, p, q = extGcd(m1, m2)
        if (b2 - b1) % d != 0:
            return 0, -1
        tmp = (b2 - b1) // d * p % (m2 // d)
        b1 += m1 * tmp
        m1 *= m2 // d
    return b1 % m1, m1
