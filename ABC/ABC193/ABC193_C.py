# https://atcoder.jp/contests/abc193/submissions/20528872
# C - Unexpressed
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    res = set()
    for a in range(2, n + 1):
        now = pow(a, 2)
        if now > n:
            break
        while now <= n:
            res.add(now)
            now *= a
    print(n - len(res))


if __name__ == '__main__':
    resolve()
