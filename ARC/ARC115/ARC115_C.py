# https://atcoder.jp/contests/arc115/submissions/21221040
# C - ℕ Coloring
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    res = [0] * n
    res[0] = 1
    for i in range(1, n + 1):
        init = res[i - 1]
        for j in range(i + i, n + 1, i):
            res[j - 1] = init + 1
    print(*res)


if __name__ == '__main__':
    solve()
