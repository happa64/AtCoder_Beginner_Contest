# https://atcoder.jp/contests/joi2008yo/submissions/11341567
# D - 星座探し
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    m = int(input())
    sign = [list(map(int, input().split())) for _ in range(m)]
    n = int(input())
    pic = [list(map(int, input().split())) for _ in range(n)]

    x0 = sign[0][0]
    y0 = sign[0][1]
    d = []
    for i in range(1, m):
        dx = sign[i][0] - x0
        dy = sign[i][1] - y0
        d.append([dx, dy])

    for x, y in pic:
        for dx, dy in d:
            x2 = x + dx
            y2 = y + dy
            if [x2, y2] not in pic:
                break
        else:
            print(x - x0, y - y0)


if __name__ == '__main__':
    resolve()
