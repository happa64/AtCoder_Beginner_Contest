# https://atcoder.jp/contests/arc055/submissions/14378679
# A - 数え上げ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    print(pow(10, n) + 7)


if __name__ == '__main__':
    resolve()
