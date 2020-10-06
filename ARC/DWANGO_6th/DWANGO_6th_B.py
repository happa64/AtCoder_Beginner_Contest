# https://atcoder.jp/contests/dwacon6th-prelims/submissions/17221268
# B - Fusing Slimes
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    X = list(map(int, input().split()))

    fact = 1
    for i in range(1, n):
        fact = fact * i % mod

    cnt = [0] * n
    for i in range(1, n):
        cnt[i] = (cnt[i - 1] + fact * pow(i, mod - 2, mod) % mod) % mod

    res = 0
    for i in range(1, n):
        res += (X[i] - X[i - 1]) * cnt[i]
        res %= mod
    print(res)


if __name__ == '__main__':
    resolve()
