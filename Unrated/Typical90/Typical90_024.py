# https://atcoder.jp/contests/typical90/submissions/22271793
# 024 - Select +／- One（★2）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = sum(abs(a - b) for a, b in zip(A, B))
    if cnt > k:
        print("No")
    else:
        diff = k - cnt
        print("Yes" if diff % 2 == 0 else "No")


if __name__ == '__main__':
    solve()
