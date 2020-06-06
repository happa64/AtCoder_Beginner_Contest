# https://atcoder.jp/contests/abc014/submissions/14045469
# A - けんしょう先生のお菓子配り
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a = int(input())
    b = int(input())

    res = 0 if a % b == 0 else b - (a % b)
    print(res)


if __name__ == '__main__':
    resolve()
