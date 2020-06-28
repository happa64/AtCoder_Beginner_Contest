# https://atcoder.jp/contests/indeednow-quala/submissions/14799784
# A - 掛け算の筆算
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a = input()
    b = input()
    print(len(a) * len(b))


if __name__ == '__main__':
    resolve()
