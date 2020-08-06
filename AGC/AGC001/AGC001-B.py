# https://atcoder.jp/contests/agc001/submissions/15715893
# B - Mysterious Light
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, x = map(int, input().split())
    n -= x
    res = 0
    while x != 0:
        q, r = divmod(n, x)
        res += q * x * 3
        n = x
        x = r
    print(res)


if __name__ == '__main__':
    resolve()
