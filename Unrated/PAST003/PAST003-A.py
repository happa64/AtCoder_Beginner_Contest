# https://atcoder.jp/contests/past202005-open/submissions/14079299
# A - ケース・センシティブ
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    t = input()

    print("same" if s == t else "case-insensitive" if s.upper() == t.upper() else "different")


if __name__ == '__main__':
    resolve()
