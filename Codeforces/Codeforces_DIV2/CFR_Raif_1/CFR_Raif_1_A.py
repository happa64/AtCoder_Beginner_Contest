# https://codeforces.com/contest/1428/submission/95742728
# A. Box is Pull
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    t = int(input())
    for _ in range(t):
        x1, y1, x2, y2 = map(int, input().split())
        diff_x = abs(x1 - x2)
        diff_y = abs(y1 - y2)
        if not diff_x and diff_y:
            print(diff_y)
        elif diff_x and not diff_y:
            print(diff_x)
        elif not diff_x and not diff_y:
            print(0)
        else:
            print(diff_x + diff_y + 2)


if __name__ == '__main__':
    resolve()
