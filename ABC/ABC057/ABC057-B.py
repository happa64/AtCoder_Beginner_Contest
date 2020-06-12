# https://atcoder.jp/contests/abc057/submissions/14186484
# B - Checkpoints
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(n)]
    CD = [list(map(int, input().split())) for _ in range(m)]

    for a, b in AB:
        min_dist = f_inf
        res = 0
        for i in range(m):
            c, d = CD[i]
            dist = abs(a - c) + abs(b - d)
            if min_dist > dist:
                min_dist = dist
                res = i + 1
        print(res)


if __name__ == '__main__':
    resolve()
