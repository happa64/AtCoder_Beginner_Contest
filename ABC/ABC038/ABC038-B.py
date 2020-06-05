# https://atcoder.jp/contests/abc038/submissions/14015201
# B - ディスプレイ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    h1, w1 = map(int, input().split())
    h2, w2 = map(int, input().split())

    if h1 == h2 or w1 == w2 or h1 == w2 or h2 == w1:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    resolve()
