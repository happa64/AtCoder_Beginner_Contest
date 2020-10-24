# https://atcoder.jp/contests/discovery2016-final/submissions/17597232
# A - DISCO presents ディスカバリーチャンネルプログラミングコンテスト 2016 Ⅱ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    res = [0] * n
    for i in range(1, n + 1):
        idx = int(input())
        if i == 1:
            res[idx - 1] = 10 ** 5
        elif i == 2:
            res[idx - 1] = 5 * 10 ** 4
        elif i == 3:
            res[idx - 1] = 3 * 10 ** 4
        elif i == 4:
            res[idx - 1] = 2 * 10 ** 4
        elif i == 5:
            res[idx - 1] = 10 ** 4
        else:
            res[idx - 1] = 0
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
