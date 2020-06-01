# https://atcoder.jp/contests/abc169/submissions/13872567
# E - Count Median
import sys
from statistics import median

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A, B = [], []
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    am = median(A)
    bm = median(B)
    print(int(abs(bm - am) + 1) if n % 2 else int(abs((bm - am) * 2) + 1))


if __name__ == '__main__':
    resolve()
