# https://atcoder.jp/contests/agc016/submissions/16466372
# B - Colorful Hats
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    MAX = max(A)
    MIN = min(A)
    if MAX == MIN:
        print("Yes" if MAX + 1 == n or 2 * MAX <= n else "No")
    elif MAX - MIN == 1:
        cnt = A.count(MIN)
        print("Yes" if cnt < MAX and cnt + 2 * (MAX - cnt) <= n else "No")
    else:
        print("No")


if __name__ == '__main__':
    resolve()
