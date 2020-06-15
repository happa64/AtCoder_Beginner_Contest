# https://atcoder.jp/contests/arc053/submissions/14378736
# A - ドミノ色塗り
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    print(((H - 1) * W) + ((W - 1) * H))


if __name__ == '__main__':
    resolve()
