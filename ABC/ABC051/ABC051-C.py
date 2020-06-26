# https://atcoder.jp/contests/abc051/submissions/11658033
# C - Back and Forth
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    sx, sy, tx, ty = map(int, input().split())

    res = []
    for i in range(abs(ty - sy)):
        res.append("U")
    for i in range(abs(tx - sx)):
        res.append("R")
    for i in range(abs(sy - ty)):
        res.append("D")
    for i in range(abs(tx - sx) + 1):
        res.append("L")
    for i in range(abs(ty - sy) + 1):
        res.append("U")
    for i in range(abs(tx - sx) + 1):
        res.append("R")
    res.append("D")
    res.append("R")
    for i in range(abs(ty - sy) + 1):
        res.append("D")
    for i in range(abs(tx - sx) + 1):
        res.append("L")
    res.append("U")
    print("".join(res))


if __name__ == '__main__':
    resolve()
