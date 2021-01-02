# https://atcoder.jp/contests/abc187/submissions/19123871
# B - Gentle Pairs
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    for i in range(n):
        x1, y1 = XY[i]
        for j in range(i + 1, n):
            x2, y2 = XY[j]
            if -abs(x2 - x1) <= abs(y2 - y1) and abs(y2 - y1) <= abs(x2 - x1):
                res += 1
    print(res)


if __name__ == '__main__':
    resolve()
