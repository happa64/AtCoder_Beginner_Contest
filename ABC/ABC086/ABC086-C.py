# https://atcoder.jp/contests/abc086/submissions/13665772
# C - Traveling
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]
    px, py, pt = 0, 0, 0
    for i in range(n):
        t, x, y = XY[i]
        if abs(x - px) + abs(y - py) > abs(t - pt):
            print("No")
            break
        else:
            if (abs(x - px) + abs(y - py) - abs(t - pt)) % 2 != 0:
                print("No")
                break
            px, py, pt = x, y, t
    else:
        print("Yes")


if __name__ == '__main__':
    resolve()
