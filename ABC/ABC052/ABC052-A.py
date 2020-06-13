# https://atcoder.jp/contests/abc052/submissions/14206537
# A - Two Rectangles
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c, d = map(int, input().split())
    print(max(a * b, c * d))


if __name__ == '__main__':
    resolve()
