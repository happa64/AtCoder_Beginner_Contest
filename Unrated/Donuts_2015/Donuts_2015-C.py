# https://atcoder.jp/contests/donuts-2015/submissions/16488573
# C - 行列のできるドーナツ屋
import sys
from collections import deque
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    H = list(map(int, input().split()))

    que = deque([])
    imos = [0] * (n + 1)
    for i in range(n):
        while que and que[-1] < H[i]:
            que.pop()
            imos[i + 1] -= 1
        imos[i + 1] += 1
        que.append(H[i])
    res = list(accumulate(imos))[:n]
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
