# https://atcoder.jp/contests/past202010-open/submissions/18010682
# B - 電卓
import sys
import math

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y = map(int, input().split())
    if y == 0:
        print("ERROR")
    else:
        res = math.floor(x * 100 / y)
        print("{:.2f}".format(res / 100))


if __name__ == '__main__':
    resolve()
