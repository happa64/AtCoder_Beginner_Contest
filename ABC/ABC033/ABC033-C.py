# https://atcoder.jp/contests/abc033/submissions/13593078
# C - 数式の書き換え
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input().split("+")

    res = 0
    for s in S:
        if eval(s) != 0:
            res += 1

    print(res)


if __name__ == '__main__':
    resolve()
