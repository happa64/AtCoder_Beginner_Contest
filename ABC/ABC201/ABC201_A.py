# https://atcoder.jp/contests/abc201/submissions/22596084
# A - Tiny Arithmetic Sequence
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    A = list(map(int, input().split()))
    A.sort()

    if A[1] - A[0] == A[2] - A[1]:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    solve()
