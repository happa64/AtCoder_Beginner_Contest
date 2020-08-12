# https://atcoder.jp/contests/agc047/submissions/15829870
# A - Integer Product
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7
MAX = 50


def resolve():
    n = int(input())

    D = [[0] * MAX for _ in range(MAX)]
    for _ in range(n):
        a = int(round(float(input()) * 10 ** 9))
        t = a
        x = 0
        while t % 2 == 0:
            t //= 2
            x += 1
        t = a
        y = 0
        while t % 5 == 0:
            t //= 5
            y += 1
        D[x][y] += 1

    res = 0
    for x1 in range(MAX):
        for y1 in range(MAX):
            for x2 in range(max(0, 18 - x1), MAX):
                for y2 in range(max(0, 18 - y1), MAX):
                    if x1 == x2 and y1 == y2:
                        res += D[x1][y1] * (D[x1][y1] - 1)
                    else:
                        res += D[x1][y1] * D[x2][y2]
    print(res // 2)


if __name__ == '__main__':
    resolve()
