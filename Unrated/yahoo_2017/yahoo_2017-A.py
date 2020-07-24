# https://atcoder.jp/contests/yahoo-procon2017-qual/submissions/15395224
# A - Yahoo
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    print("YES" if sorted(s) == sorted(list("yahoo")) else "NO")


if __name__ == '__main__':
    resolve()
