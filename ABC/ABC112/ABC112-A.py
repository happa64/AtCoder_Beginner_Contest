# https://atcoder.jp/contests/abc112/tasks/abc112_a
# A - Programming Education
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    if n == 1:
        print("Hello World")
    else:
        a = int(input())
        b = int(input())
        print(a + b)


if __name__ == '__main__':
    resolve()
