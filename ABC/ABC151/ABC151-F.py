# https://atcoder.jp/contests/abc151/submissions/17381362
# F - Enclose All
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def calc_dist(p1, p2):
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        return pow(dx * dx + dy * dy, 0.5)

    def f(x, y):
        res = 0
        for i in range(n):
            res = max(res, calc_dist([x, y], XY[i]))
        return res

    def g(x):
        left, right = 0, 1000
        while abs(left - right) > 10 ** -9:
            mid_left = (left * 2 + right) / 3
            mid_right = (left + right * 2) / 3
            if f(x, mid_left) > f(x, mid_right):
                left = mid_left
            else:
                right = mid_right
        return f(x, left)

    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]

    left, right = 0, 1000
    while abs(left - right) > 10 ** -9:
        mid_left = (left * 2 + right) / 3
        mid_right = (left + right * 2) / 3
        if g(mid_left) > g(mid_right):
            left = mid_left
        else:
            right = mid_right
    ans = g(left)
    print(ans)


if __name__ == '__main__':
    resolve()
