# https://atcoder.jp/contests/joi2013yo/submissions/15075989
# A - 宿題 (Homework)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    L = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())

    t = max((A + C - 1) // C, (B + D - 1) // D)
    print(L - t)


if __name__ == '__main__':
    resolve()
