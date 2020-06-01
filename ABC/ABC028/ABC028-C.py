# https://atcoder.jp/contests/abc028/submissions/13909313
# C - 数を3つ選ぶマン
import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    NUM = list(map(int, input().split()))

    res = set()
    for pattern in combinations(NUM, 3):
        total = sum(pattern)
        res.add(total)

    res = sorted(list(res), reverse=True)
    print(res[2])


if __name__ == '__main__':
    resolve()
