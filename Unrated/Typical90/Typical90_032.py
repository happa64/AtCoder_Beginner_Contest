# https://atcoder.jp/contests/typical90/submissions/22327652
# 032 - AtCoder Ekiden（★3）
import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    XY = set(tuple(map(int, input().split())) for _ in range(m))

    res = f_inf
    for pattern in permutations(range(n)):
        t = A[pattern[0]][0]
        for i in range(1, n):
            x, y = pattern[i - 1], pattern[i]
            if (x + 1, y + 1) in XY or (y + 1, x + 1) in XY:
                break
            t += A[y][i]
        else:
            res = min(res, t)
    print(res if res != f_inf else -1)


if __name__ == '__main__':
    solve()
