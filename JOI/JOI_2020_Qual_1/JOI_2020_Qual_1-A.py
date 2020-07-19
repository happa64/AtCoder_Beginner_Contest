# https://atcoder.jp/contests/joi2020yo1a/submissions/15316354
# A - 3 つの整数 (Three Integers)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    ABC = list(input().split())
    one = ABC.count("1")
    two = ABC.count("2")
    print(1 if one > two else 2)


if __name__ == '__main__':
    resolve()
