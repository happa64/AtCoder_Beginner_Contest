# https://atcoder.jp/contests/arc001/submissions/15662565
# C - パズルのお手伝い
import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    C = [list(input()) for _ in range(8)]

    RC = []
    for i in range(8):
        for j in range(8):
            if C[i][j] == "Q":
                RC.append((i, j))

    res = [["."] * 8 for _ in range(8)]
    for pattern in permutations(list(range(8))):
        XY = set(tuple((idx, num) for idx, num in enumerate(pattern)))
        flg = True
        for r, c in RC:
            if (r, c) not in XY:
                flg = False
                break
        if not flg:
            continue

        for x, y in XY:
            for i in range(1, 8):
                if (x + i, y + i) in XY or (x + i, y - i) in XY or (x - i, y + i) in XY or (
                x - i, y - i) in XY:
                    flg = False
                    break
            else:
                continue
            break
        if flg:
            for x, y in XY:
                res[x][y] = "Q"
            for i in res:
                print("".join(i))
            break
    else:
        print("No Answer")


if __name__ == '__main__':
    resolve()
