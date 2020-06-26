# https://atcoder.jp/contests/tenka1-2012-qualB/submissions/14691125
# A - 孫子算経
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())

    for i in range(1, 128):
        if i % 3 == a and i % 5 == b and i % 7 == c:
            print(i)


if __name__ == '__main__':
    resolve()
