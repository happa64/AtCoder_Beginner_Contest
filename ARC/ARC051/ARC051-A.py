# https://atcoder.jp/contests/arc051/submissions/13494950
# A - 塗り絵
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x1, y1, r = map(int, input().split())
    x2, y2, x3, y3 = map(int, input().split())

    # 〇が□に内包されているか？
    print("NO" if x2 <= x1 - r and x1 + r <= x3 and y2 <= y1 - r and y1 + r <= y3 else "YES")
    # □が〇に内包されているか？
    print("NO" if (x3 - x1) ** 2 + (y3 - y1) ** 2 <= r ** 2 and (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r ** 2 and \
                  (x3 - x1) ** 2 + (y2 - y1) ** 2 <= r ** 2 and (x2 - x1) ** 2 + (y3 - y1) ** 2 <= r ** 2 else "YES")


if __name__ == '__main__':
    resolve()
