# https://atcoder.jp/contests/past202004-open/tasks/past202004_c
# C - 山崩し
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = [list(input()) for _ in range(n)]

    w = 2 * n - 1
    # 一番下から見ていく
    for i in reversed(range(n)):
        for j in range(w):
            if S[i][j] == "#":
                for di, dj in ((1, -1), (1, 0), (1, 1)):
                    next_i, next_j = i + di, j + dj
                    if 0 <= next_i < n and 0 <= next_j < w:
                        if S[next_i][next_j] == "X":
                            S[i][j] = "X"
                            break

    for i in S:
        print("".join(i))


if __name__ == '__main__':
    resolve()
