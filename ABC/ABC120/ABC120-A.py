# https://atcoder.jp/contests/abc120/submissions/12897126
# A - Favorite Sound
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())
    if c * a <= b:
        print(c)
    else:
        print(b // a)



if __name__ == '__main__':
    resolve()
