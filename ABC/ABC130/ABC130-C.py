# https://atcoder.jp/contests/abc130/submissions/13431375
# C - Rectangle Cutting
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要：
        どこに点を取っても、最小の面積の最大値は、長方形の面積の半分となる。
        また、点が長方形の中央にある場合のみ、分割方法が複数ある。

    計算量；O(1)
    """
    w, h, x, y = map(int, input().split())

    print(w * h / 2, int(x * 2 == w and y * 2 == h))


if __name__ == '__main__':
    resolve()
