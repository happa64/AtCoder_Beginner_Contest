# https://atcoder.jp/contests/arc021/submissions/14512294
# A - DEAD END
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A = [list(map(int, input().split())) for _ in range(4)]

    for h in range(4):
        for w in range(4):
            for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_h, next_w = h + dh, w + dw
                if next_h < 0 or next_h >= 4 or next_w < 0 or next_w >= 4:
                    continue
                if A[h][w] == A[next_h][next_w]:
                    print("CONTINUE")
                    exit()
    print("GAMEOVER")


if __name__ == '__main__':
    resolve()
