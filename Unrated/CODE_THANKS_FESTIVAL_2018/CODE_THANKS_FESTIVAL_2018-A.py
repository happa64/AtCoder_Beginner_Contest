# https://atcoder.jp/contests/code-thanks-festival-2018-open/submissions/15390633
# A - Two Problems
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    t, a, b, c, d = map(int, input().split())

    if a + c <= t:
        print(b + d)
    elif a <= t and c <= t:
        print(max(b, d))
    elif a <= t:
        print(b)
    elif c <= t:
        print(d)
    else:
        print(0)


if __name__ == '__main__':
    resolve()
