# https://atcoder.jp/contests/abc044/submissions/14186341
# A - 高橋君とホテルイージー
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())

    res = min(n, k) * x + max(0, (n - k) * y)
    print(res)


if __name__ == '__main__':
    resolve()
