# https://atcoder.jp/contests/tenka1-2014-quala/submissions/14691165
# A - 天下一序数
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    num = sorted([str(i) for i in range(1, 1001)])
    print(*num, sep="\n")


if __name__ == '__main__':
    resolve()
