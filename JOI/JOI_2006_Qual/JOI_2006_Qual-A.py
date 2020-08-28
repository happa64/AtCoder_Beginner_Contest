# https://atcoder.jp/contests/joi2006yo/submissions/16277964
# A - JOI 2006 予選 問題1
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = B = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if a > b:
            A += a + b
        elif a < b:
            B += a + b
        else:
            A += a
            B += b
    print(A, B)


if __name__ == '__main__':
    resolve()
