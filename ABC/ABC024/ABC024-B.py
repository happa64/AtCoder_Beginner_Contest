# https://atcoder.jp/contests/abc024/submissions/13993201
# B - 自動ドア
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, t = map(int, input().split())
    A = list(int(input()) for _ in range(n))

    res = 0
    for i in range(n - 1):
        res += t if A[i + 1] - A[i] >= t else A[i + 1] - A[i]

    print(res + t)


if __name__ == '__main__':
    resolve()
