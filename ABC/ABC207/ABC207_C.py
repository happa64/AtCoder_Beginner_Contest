# https://atcoder.jp/contests/abc207/submissions/23781224
# C - Many Segments
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def check(t, l, r):
    if t == 1:
        return l, r
    elif t == 2:
        return l, r - 0.1
    elif t == 3:
        return l + 0.1, r
    else:
        return l + 0.1, r - 0.1


def solve():
    n = int(input())
    section = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    for i in range(n):
        t1, l1, r1 = section[i]
        a, b = check(t1, l1, r1)
        for j in range(i + 1, n):
            t2, l2, r2 = section[j]
            x, y = check(t2, l2, r2)
            if x <= b and a <= y:
                res += 1
    print(res)


if __name__ == '__main__':
    solve()
