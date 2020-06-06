# https://atcoder.jp/contests/abc016/submissions/14054245
# D - 一刀両断
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]

    # 解は(軌道と木の板の辺が交わる回数)//2+1である
    cnt = 0
    x3, y3 = XY[0]
    for i in range(1, n + 1):
        x4, y4 = XY[0] if i == n else XY[i]
        # 軌道と木の板の辺が交わる条件
        if ((x1 - x2) * (y3 - y1) + (y1 - y2) * (x1 - x3)) * ((x1 - x2) * (y4 - y1) + (y1 - y2) * (x1 - x4)) < 0:
            if ((x3 - x4) * (y1 - y3) + (y3 - y4) * (x3 - x1)) * ((x3 - x4) * (y2 - y3) + (y3 - y4) * (x3 - x2)) < 0:
                cnt += 1
        x3, y3 = x4, y4

    print(cnt // 2 + 1)


if __name__ == '__main__':
    resolve()
