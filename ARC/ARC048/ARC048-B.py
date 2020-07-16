# https://atcoder.jp/contests/arc048/submissions/15275732
# B - AtCoderでじゃんけんを
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    RH = [list(map(int, input().split())) for _ in range(n)]

    MAX_RATE = 10 ** 5 + 1
    rate = [[0] * 3 for _ in range(MAX_RATE)]
    rate_cnt = [0] * MAX_RATE
    for r, h in RH:
        rate_cnt[r] += 1
        rate[r][h - 1] += 1
    acc_rate_cnt = list(accumulate(rate_cnt))

    res = [[0] * 3 for _ in range(n)]
    for i in range(n):
        r, h = RH[i]
        g, c, p = rate[r]
        win = c if h == 1 else p if h == 2 else g
        lose = p if h == 1 else g if h == 2 else c
        draw = g - 1 if h == 1 else c - 1 if h == 2 else p - 1
        win += acc_rate_cnt[r - 1]
        lose += acc_rate_cnt[MAX_RATE - 1] - acc_rate_cnt[r]
        res[i][0] += win
        res[i][1] += lose
        res[i][2] = draw

    for i in res:
        print(*i)


if __name__ == '__main__':
    resolve()
