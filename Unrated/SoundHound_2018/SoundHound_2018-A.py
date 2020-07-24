# https://atcoder.jp/contests/soundhound2018/submissions/15394983
# A - SoundHound
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y = input().split()
    print("YES" if x[0] == "S" and y[0] == "H" else "NO")


if __name__ == '__main__':
    resolve()
