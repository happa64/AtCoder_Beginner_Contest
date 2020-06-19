# https://atcoder.jp/contests/abc148/submissions/14463483
# E - Double Factorial
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    if n % 2 != 0:
        print(0)
        exit()

    L = n // 2
    res = 0
    while L:
        res += L // 5
        L //= 5
    print(res)


if __name__ == '__main__':
    resolve()
