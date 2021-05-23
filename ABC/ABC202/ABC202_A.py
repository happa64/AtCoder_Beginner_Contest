# https://atcoder.jp/contests/abc202/submissions/22791396
# A - Three Dice
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    a, b, c = map(int, input().split())
    res = (7 - a) + (7 - b) + (7 - c)
    print(res)


if __name__ == '__main__':
    solve()
