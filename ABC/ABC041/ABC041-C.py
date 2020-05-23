# https://atcoder.jp/contests/abc041/submissions/13493856
# C - 背の順
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list([idx + 1, int(a)] for idx, a in enumerate(input().split()))

    A = sorted(A, key=lambda x: x[1], reverse=True)

    for j in range(n):
        print(A[j][0])


if __name__ == '__main__':
    resolve()
