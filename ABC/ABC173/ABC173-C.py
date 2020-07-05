# https://atcoder.jp/contests/abc173/submissions/14984122
# C - H and V
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W, k = map(int, input().split())
    grid = list(list(input()) for _ in range(H))

    res = 0
    for pattern_H in product([0, 1], repeat=H):
        ign_H = []
        for idx, p in enumerate(pattern_H):
            if p == 1:
                ign_H.append(idx)
        for pattern_W in product([0, 1], repeat=W):
            cnt = 0
            ign_W = []
            for idx, p in enumerate(pattern_W):
                if p == 1:
                    ign_W.append(idx)
            for h in range(H):
                if h in ign_H:
                    continue
                for w in range(W):
                    if w in ign_W:
                        continue
                    if grid[h][w] == "#":
                        cnt += 1
            if cnt == k:
                res += 1
    print(res)


if __name__ == '__main__':
    resolve()
