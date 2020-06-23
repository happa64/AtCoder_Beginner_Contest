# https://atcoder.jp/contests/arc031/submissions/14638755
# A - 名前
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    name = input()

    print("YES" if name == name[::-1] else "NO")


if __name__ == '__main__':
    resolve()
