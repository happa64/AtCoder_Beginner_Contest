# https://atcoder.jp/contests/colopl2018-qual/submissions/15394526
# A - すぬけそだて――登録――
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    s = input()
    print("YES" if a <= len(s) <= b else "NO")


if __name__ == '__main__':
    resolve()
