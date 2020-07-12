# https://atcoder.jp/contests/joi2017yo/submissions/15203480
# B - ポイントカード (Point Card)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(m)]

    res = []
    for a, b in AB:
        res.append(0 if a >= n else n - a)
    res.sort()
    print(sum(res[:m - 1]))


if __name__ == '__main__':
    resolve()
