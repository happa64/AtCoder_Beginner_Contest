# https://atcoder.jp/contests/abc058/submissions/13429773
# A - ι⊥l
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())

    print("YES" if b - a == c - b else "NO")


if __name__ == '__main__':
    resolve()
