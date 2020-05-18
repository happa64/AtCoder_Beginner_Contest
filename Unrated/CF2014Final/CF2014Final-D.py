# https://atcoder.jp/contests/code-festival-2014-final/submissions/13151317
# D - パスカルの三角形
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要：
        パスカルの三角形を見た時、2行目以降の2列目が1,2,3,4,5,6,7,…となっている事がわかる。
        つまり、AはA+1行目の2列目に必ず出現する。

    計算量；O(1)
    """
    a = int(input())
    print(a + 1, 2)


if __name__ == '__main__':
    resolve()
