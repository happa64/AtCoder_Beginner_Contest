# https://atcoder.jp/contests/abc188/submissions/19314922
# B - Orthogonality
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    tot = 0
    for a, b in zip(A, B):
        tot += a * b
    print("Yes" if tot == 0 else "No")


if __name__ == '__main__':
    resolve()
