# https://atcoder.jp/contests/arc014/submissions/14484212
# A - 君が望むなら世界中全てのたこ焼きを赤と青に染め上げよう
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    print("Blue" if n % 2 == 0 else "Red")


if __name__ == '__main__':
    resolve()
