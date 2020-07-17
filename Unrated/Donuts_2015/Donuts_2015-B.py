# https://atcoder.jp/contests/donuts-2015/submissions/15285476
# B - Tokyo 7th シスターズ
import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = [list(map(int, input().split())) for _ in range(m)]

    res = 0
    for unit in combinations(list(range(1, n + 1)), 9):
        point = sum([A[i - 1] for i in unit])
        unit = set(unit)
        for bonus, _, *idols in B:
            cnt = 0
            for idol in idols:
                if idol in unit:
                    cnt += 1
            if cnt >= 3:
                point += bonus
        res = max(res, point)
    print(res)


if __name__ == '__main__':
    resolve()
