# https://atcoder.jp/contests/abc034/submissions/14152026
# A - テスト
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y = map(int, input().split())
    print("Better" if x < y else "Worse")


if __name__ == '__main__':
    resolve()
