# https://atcoder.jp/contests/arc015/submissions/14484231
# A - Celsius と Fahrenheit
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    print(9 / 5 * n + 32)


if __name__ == '__main__':
    resolve()
