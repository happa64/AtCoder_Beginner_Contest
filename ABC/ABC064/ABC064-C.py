# https://atcoder.jp/contests/abc064/submissions/13926241
# C - Colorful Leaderboard
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    Color = [0] * 9
    for a in A:
        if a >= 3200:
            Color[-1] += 1
        else:
            Color[a // 400] = 1

    mi = sum(Color[:8]) + (1 if sum(Color[:8]) == 0 and Color[8] > 0 else 0)
    ma = sum(Color[:8]) + Color[8]

    print(mi, ma)


if __name__ == '__main__':
    resolve()
