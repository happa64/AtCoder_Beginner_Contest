# https://atcoder.jp/contests/abc016/submissions/13970350
# B - A±B Problem
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())

    if a + b == c and a - b == c:
        print("?")
    elif a + b == c:
        print("+")
    elif a - b == c:
        print("-")
    else:
        print("!")


if __name__ == '__main__':
    resolve()
