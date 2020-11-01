# https://atcoder.jp/contests/abc181/submissions/17791245
# C - Collinearity
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        x1, y1 = XY[i]
        for j in range(i + 1, n):
            x2, y2 = XY[j]
            for k in range(j + 1, n):
                x3, y3 = XY[k]
                area = ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
                if area == 0:
                    print("Yes")
                    exit()
    print("No")


if __name__ == '__main__':
    resolve()
