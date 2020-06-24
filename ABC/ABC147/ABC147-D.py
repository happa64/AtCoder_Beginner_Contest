# https://atcoder.jp/contests/abc147/submissions/14160404
# D - Xor Sum 4
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = 0
    for i in range(60):
        cnt = 0
        for a in A:
            cnt += (a >> i) & 1
        res += (cnt * (n - cnt) % mod) * (1 << i) % mod
        res %= mod
    print(res)


if __name__ == '__main__':
    resolve()
