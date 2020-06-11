# https://atcoder.jp/contests/arc041/submissions/14168478
# B - アメーバ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    B = list(list(input()) for _ in range(H))

    A = [["0"] * W for _ in range(H)]
    for h in range(1, H - 1):
        for w in range(1, W - 1):
            cnt = f_inf
            for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_h, next_w = h + dh, w + dw
                cnt = min(cnt, int(B[next_h][next_w]))
            A[h][w] = str(cnt)
            for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_h, next_w = h + dh, w + dw
                B[next_h][next_w] = int(B[next_h][next_w]) - cnt

    for a in A:
        print("".join(a))


if __name__ == '__main__':
    resolve()
