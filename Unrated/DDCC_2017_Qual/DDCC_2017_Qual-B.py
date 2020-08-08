# https://atcoder.jp/contests/ddcc2017-qual/submissions/15761709
# B - 鉛筆
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c, d = map(int, input().split())
    res = c * 12 + b * 144 + a * 1728 + d
    print(res)


if __name__ == '__main__':
    resolve()
