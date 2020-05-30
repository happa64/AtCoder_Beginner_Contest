# https://atcoder.jp/contests/m-solutions2019/submissions/13700438
# B - Sumo
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input().rstrip()
    k = len(s)
    win = s.count("o")
    print("YES" if 15 - k >= 8 - win else "NO")


if __name__ == '__main__':
    resolve()
