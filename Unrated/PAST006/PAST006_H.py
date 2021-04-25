# https://atcoder.jp/contests/past202104-open/submissions/22052161
# H - カンカンマート
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, m, k, q = map(int, input().split())
    S, T = [], []
    for _ in range(n):
        p, t = map(int, input().split())
        T.append(p) if t == 0 else S.append(p)
    S.sort()
    T.sort()
    SR = [0] + list(accumulate(S))
    TR = [0] + list(accumulate(T))

    res = f_inf
    for i in range(min(m + 1, len(S) + 1)):
        s = SR[i] + ((i + k - 1) // k) * q
        j = m - i
        if len(T) < j:
            continue
        t = TR[j]
        res = min(res, s + t)
    print(res)


if __name__ == '__main__':
    solve()
