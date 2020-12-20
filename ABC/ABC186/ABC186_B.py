# https://atcoder.jp/contests/abc186/submissions/18864118
# B - Blocks on Grid
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    mi = min([A[h][w] for h in range(H) for w in range(W)])

    res = 0
    for h in range(H):
        for w in range(W):
            if mi < A[h][w]:
                res += A[h][w] - mi
    print(res)


if __name__ == '__main__':
    resolve()
