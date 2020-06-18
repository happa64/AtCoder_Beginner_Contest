# https://atcoder.jp/contests/arc002/submissions/14445912
# A - うるう年
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    y = int(input())

    if y % 400 == 0:
        print("YES")
    elif y % 100 == 0:
        print("NO")
    elif y % 4 == 0:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    resolve()
