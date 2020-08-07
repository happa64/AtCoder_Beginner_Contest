# https://atcoder.jp/contests/nikkei2019-final/submissions/15734926
# B - Big Integers
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if n < m:
        print("X")
    elif n > m:
        print("Y")
    else:
        for a, b in zip(A, B):
            if a < b:
                print("X")
                break
            elif a > b:
                print("Y")
                break
        else:
            print("Same")


if __name__ == '__main__':
    resolve()
