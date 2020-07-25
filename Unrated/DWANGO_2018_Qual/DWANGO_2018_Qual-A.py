# https://atcoder.jp/contests/dwacon2018-prelims/submissions/15406971
# A - ニコニコ文字列判定
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    if s[0] == s[2] and s[1] == s[3]:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    resolve()
