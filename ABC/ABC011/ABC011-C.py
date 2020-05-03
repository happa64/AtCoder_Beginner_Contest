# https://atcoder.jp/contests/abc011/tasks/abc011_3
# C - 123引き算
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    NG = list(int(input()) for _ in range(3))

    if n in NG:
        print("NO")
        exit()

    # 貪欲法
    # 3,2,1の順でNGにならない数値を引いていく
    for _ in range(100):
        if n - 3 not in NG and n >= 3:
            n -= 3
        elif n - 2 not in NG and n >= 2:
            n -= 2
        elif n - 1 not in NG and n >= 1:
            n -= 1

    if n == 0:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    resolve()
