# https://atcoder.jp/contests/abc181/submissions/17784069
# B - Trapezoid Sum
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    AB = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    for a, b in AB:
        res += (a + b) * (b - a + 1) // 2

    print(res)


if __name__ == '__main__':
    resolve()
