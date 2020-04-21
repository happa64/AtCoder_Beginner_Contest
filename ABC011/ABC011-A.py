# https://atcoder.jp/contests/abc011/tasks/abc011_1
# A - 来月は何月？
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    if n < 12:
        print(n + 1)
    else:
        print(1)


if __name__ == '__main__':
    resolve()
