# https://atcoder.jp/contests/abc077/submissions/14004206
# A - Rotation
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    print("YES" if input() == input()[::-1] else "NO")


if __name__ == '__main__':
    resolve()
