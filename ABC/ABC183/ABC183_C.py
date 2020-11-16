# https://atcoder.jp/contests/abc183/submissions/18130016
# C - Travel
import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    for pattern in permutations(range(n)):
        if pattern[-1] != 0:
            continue
        dist = 0
        now = 0
        for num in pattern:
            dist += T[now][num]
            now = num
        if dist == k:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
