# https://atcoder.jp/contests/arc116/submissions/21441151
# B - Products of Min-Max
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 998244353


def solve():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()

    pow2_mod = [1]
    for i in range(1, n + 1):
        pow2_mod.append(pow2_mod[-1] * 2 % MOD)

    tot = 0
    for i in range(1, n):
        tot += A[i] * pow2_mod[max(0, i - 1)] % MOD
        tot %= MOD

    res = 0
    for i in range(n):
        res += A[i] * (A[i] + tot)
        res %= MOD
        if i + 1 < n:
            tot -= A[i + 1]
        tot = tot * pow(2, MOD - 2, MOD) % MOD
    print(res)


if __name__ == '__main__':
    solve()
