# https://atcoder.jp/contests/nikkei2019-ex/submissions/15498227
# A - Prefix Array
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    n = len(S)
    for i in range(1, n):
        print(i)


if __name__ == '__main__':
    resolve()
