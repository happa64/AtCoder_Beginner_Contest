# https://atcoder.jp/contests/joi2015yo/submissions/15862554
# A - 水道料金 (Water Rate)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    P = int(input())

    res1 = P * A
    res2 = B + max(0, P - C) * D
    print(min(res1, res2))


if __name__ == '__main__':
    resolve()
