# https://atcoder.jp/contests/abc209/submissions/24106347
# B - Can you buy them all?
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(n):
        if i % 2:
            x -= A[i] - 1
        else:
            x -= A[i]

    if x >= 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    solve()
