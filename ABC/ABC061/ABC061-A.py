# https://atcoder.jp/contests/abc061/submissions/14267101
# A - Between Two Integers
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A, B, C = map(int, input().split())
    if A <= C <= B:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    resolve()
