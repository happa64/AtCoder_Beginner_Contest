# https://atcoder.jp/contests/joi2014yo/submissions/15124733
# C - 超都観光 (Super Metropolis)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    W, H, N = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    prev_x, prev_y = XY[0]
    for i in range(1, N):
        next_x, next_y = XY[i]
        if (prev_x < next_x and prev_y < next_y) or (prev_x > next_x and prev_y > next_y):
            res += max(abs(next_x - prev_x), abs(next_y - prev_y))
        else:
            res += abs(next_x - prev_x) + abs(next_y - prev_y)
        prev_x, prev_y = next_x, next_y
    print(res)


if __name__ == '__main__':
    resolve()
