# https://atcoder.jp/contests/exawizards2019/submissions/13700571
# B - Red or Blue
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input().rstrip()

    r = s.count("R")
    b = s.count("B")
    print("Yes" if r > b else "No")


if __name__ == '__main__':
    resolve()
