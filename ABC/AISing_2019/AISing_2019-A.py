# https://atcoder.jp/contests/aising2019/submissions/13654743
# A - Bulletin Board
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    H = int(input())
    W = int(input())

    res = (n - H + 1) * (n - W + 1)
    print(res)


if __name__ == '__main__':
    resolve()
