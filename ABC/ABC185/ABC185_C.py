# https://atcoder.jp/contests/abc185/submissions/18729660
# C - Duodecim Ferra
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    l = int(input())
    b = l - 1
    A = B = 1
    for i in range(11):
        A *= b - i
        B *= i + 1
    res = A // B
    print(res)


if __name__ == '__main__':
    resolve()
