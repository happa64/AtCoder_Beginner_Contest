# https://atcoder.jp/contests/abc190/submissions/19798674
# D - Staircase Sequences
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    MAX = int(pow(2 * n, 0.5)) + 1

    res = 0
    for i in range(1, MAX):
        t = (i - 1) * i // 2
        diff = n - t
        if diff % i == 0:
            res += 2
    print(res)


if __name__ == '__main__':
    resolve()
