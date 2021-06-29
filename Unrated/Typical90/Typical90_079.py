# https://atcoder.jp/contests/typical90/submissions/23861982
# 079 - Two by Two（★3）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]
    res = 0
    for h in range(H - 1):
        for w in range(W - 1):
            diff = B[h][w] - A[h][w]
            res += abs(diff)
            for dh, dw in ((0, 0), (1, 0), (0, 1), (1, 1)):
                nh, nw = h + dh, w + dw
                A[nh][nw] += diff
    if all(B[h][w] == A[h][w] for h in range(H) for w in range(W)):
        print("Yes")
        print(res)
    else:
        print("No")


if __name__ == '__main__':
    solve()
