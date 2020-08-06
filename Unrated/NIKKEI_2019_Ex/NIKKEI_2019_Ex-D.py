# https://atcoder.jp/contests/nikkei2019-ex/submissions/15724769
# D - 辞書順最小の数
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    print(pow(10, n - 1))


if __name__ == '__main__':
    resolve()
