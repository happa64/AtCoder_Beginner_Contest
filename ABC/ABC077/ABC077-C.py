# https://atcoder.jp/contests/arc084/submissions/14677922
# C - Snuke Festival
import sys
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = sorted(list(map(int, input().split())))

    res = 0
    for i in range(n):
        u = bisect_left(A, B[i])
        d = bisect_right(C, B[i])
        res += u * (n - d)
    print(res)


if __name__ == '__main__':
    resolve()
