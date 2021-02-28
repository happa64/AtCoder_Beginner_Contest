# https://atcoder.jp/contests/abc193/submissions/20523298
# B - Play Snuke
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    APX = [list(map(int, input().split())) for _ in range(n)]
    APX.sort(key=lambda x: x[2])

    res = f_inf
    for a, p, x in APX:
        x -= a
        if x > 0:
            res = min(res, p)
    print(res if res != f_inf else -1)


if __name__ == '__main__':
    resolve()
