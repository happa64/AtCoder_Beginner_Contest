# https://atcoder.jp/contests/joi2021yo1c/submissions/18697074
# A - 計算 (Calculation)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    print(max(a + b, a - b), min(a + b, a - b), sep="\n")


if __name__ == '__main__':
    resolve()
