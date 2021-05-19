# https://atcoder.jp/contests/typical90/submissions/22729888
# 044 - Shift and Swapping（★3）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))

    shift = 0
    for _ in range(q):
        t, x, y = map(int, input().split())
        x -= 1
        y -= 1
        if t == 1:
            x = (x + shift) % n
            y = (y + shift) % n
            A[x], A[y] = A[y], A[x]
        elif t == 2:
            shift -= 1
        else:
            print(A[(x + shift) % n])


if __name__ == '__main__':
    solve()
