# https://atcoder.jp/contests/abc028/submissions/13993481
# B - 文字数カウント
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    a = s.count("A")
    b = s.count("B")
    c = s.count("C")
    d = s.count("D")
    e = s.count("E")
    f = s.count("F")
    print(a, b, c, d, e, f)


if __name__ == '__main__':
    resolve()
