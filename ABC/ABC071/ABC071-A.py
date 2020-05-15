# https://atcoder.jp/contests/abc071/submissions/13229344
# A - Meal Delivery
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, a, b = map(int, input().split())
    print("A") if abs(x - a) < abs(x - b) else print("B")


if __name__ == '__main__':
    resolve()
