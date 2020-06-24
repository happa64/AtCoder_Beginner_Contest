# https://atcoder.jp/contests/arc102/submissions/14653220
# C - Triangular Relationship
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())

    res = pow(n // k, 3)
    if k % 2 != 0:
        print(res)
    else:
        res += pow((n + k // 2) // k, 3)
        print(res)


if __name__ == '__main__':
    resolve()
