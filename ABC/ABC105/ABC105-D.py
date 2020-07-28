# https://atcoder.jp/contests/abc105/submissions/15501627
# D - Candy Distribution
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    A_sum = [0]
    D = defaultdict(int)
    D[A_sum[-1]] += 1
    for a in A:
        A_sum.append((A_sum[-1] + a) % m)
        D[A_sum[-1]] += 1

    res = 0
    for v in D.values():
        res += v * (v - 1) // 2
    print(res)


if __name__ == '__main__':
    resolve()
