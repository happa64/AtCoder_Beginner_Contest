# https://atcoder.jp/contests/abc196/submissions/21109649
# E - Filters
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    AT = [list(map(int, input().split())) for _ in range(n)]
    _ = int(input())
    X = list(map(int, input().split()))

    l, r = -f_inf, f_inf
    s = 0
    for a, t in AT:
        if t == 1:
            s += a
            l += a
            r += a
        elif t == 2:
            l = max(l, a)
            r = max(r, a)
        else:
            r = min(r, a)
            l = min(l, a)

    for x in X:
        x += s
        if x < l:
            x = l
        if x > r:
            x = r
        print(x)


if __name__ == '__main__':
    solve()
