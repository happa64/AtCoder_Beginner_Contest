# https://atcoder.jp/contests/typical90/submissions/23912344
# 082 - Counting Numbers（★3）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    l, r = map(int, input().split())
    res = 0
    while l <= r:
        cnt = len(str(l))
        next_l = min(r, pow(10, cnt) - 1)
        diff = next_l - l + 1
        tot = cnt * (next_l + l) * diff // 2 % MOD
        res += tot
        res %= MOD
        l = next_l + 1
    print(res)


if __name__ == '__main__':
    solve()
