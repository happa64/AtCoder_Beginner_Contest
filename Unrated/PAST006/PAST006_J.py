# https://atcoder.jp/contests/past202104-open/submissions/22052228
# J - ポイントとコストと
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def calc_cost(xi, yi, p, c):
    return pow(p - xi, 2) + pow(c - yi, 2)


def solve():
    def ternary_search(high, low):
        for _ in range(100):
            mid_left = (high + low * 2) / 3
            mid_right = (high * 2 + low) / 3
            if f(mid_left) >= f(mid_right):
                low = mid_left
            else:
                high = mid_right
        return f(high)

    def f(p):
        return sum(calc_cost(x, y, p, C) for x, y in XY)

    N, C = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]

    res = ternary_search(-10 ** 5 - 1, 10 ** 5 + 1)
    print(res)


if __name__ == '__main__':
    solve()
