# https://atcoder.jp/contests/mujin-pc-2018/submissions/15394897
# A - コンテスト名
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    print("Yes" if s[:5] == "MUJIN" else "No")


if __name__ == '__main__':
    resolve()
