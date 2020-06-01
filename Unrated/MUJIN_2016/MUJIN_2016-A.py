# https://atcoder.jp/contests/mujin-pc-2016/submissions/13908356
# A - MUJIN
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    c = input()
    print("Right" if c == "O" or c == "P" or c == "K" or c == "L" else "Left")


if __name__ == '__main__':
    resolve()
