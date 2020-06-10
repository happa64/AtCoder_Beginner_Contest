# https://atcoder.jp/contests/abc035/submissions/14152085
# A - テレビ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    W, H = map(int, input().split())
    if W // 4 == H // 3:
        print("4:3")
    else:
        print("16:9")


if __name__ == '__main__':
    resolve()
