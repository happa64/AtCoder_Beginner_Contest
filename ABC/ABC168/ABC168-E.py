# https://atcoder.jp/contests/abc168/submissions/18639739
# E - ∙ (Bullet)
import sys
from math import gcd
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def to_standard_form(s, t):
    if s == 0:
        return 0, 1
    g = gcd(s, t)
    s //= g
    t //= g
    if s < 0:
        return -s, -t
    return s, t


def resolve():
    n = int(input())
    AB = [list(map(int, input().split())) for _ in range(n)]

    pow2 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow2[i] = pow2[i - 1] * 2 % mod

    X = defaultdict(int)
    Y = defaultdict(int)
    res = 0
    for a, b in AB:
        if a == b == 0:
            res += 1
            continue
        a, b = to_standard_form(a, b)
        if b <= 0:
            X[(a, b)] += 1
        else:
            X[(b, -a)] += 0
            Y[(b, -a)] += 1

    k = 1
    for key, x in X.items():
        y = Y[key]
        k *= (pow2[x] - 1) + (pow2[y] - 1) + 1
        k %= mod
    res += k - 1
    print(res % mod)


if __name__ == '__main__':
    resolve()
