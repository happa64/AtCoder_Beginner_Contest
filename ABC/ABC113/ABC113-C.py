# https://atcoder.jp/contests/abc113/submissions/12824376
# C - ID
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    PY = []
    for i in range(m):
        p, y = map(int, input().split())
        PY.append([i, p, y])
    PY = sorted(PY, key=lambda x: x[2])
    PY = sorted(PY, key=lambda x: x[1])

    res = [] * m
    prev = PY[0][1]
    last = 0
    for i in range(m):
        idx, p, y = PY[i]
        if prev != p:
            last = 1
            prev = p
        else:
            last += 1

        id = str(p).zfill(6) + str(last).zfill(6)
        res.append([idx, id])

    res = sorted(res, key=lambda x: x[0])
    for i in res:
        print(i[1])


if __name__ == '__main__':
    resolve()
