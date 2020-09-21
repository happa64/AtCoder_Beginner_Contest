# https://atcoder.jp/contests/arc048/submissions/16934563
# B - AtCoderでじゃんけんを
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    RH = [list(map(lambda x:int(x) - 1, input().split())) for _ in range(n)]
    MAX_RATE = max([r for r, _ in RH]) + 1

    hand_by_rate = [[0] * MAX_RATE for _ in range(3)]
    rate_distribution = [0] * MAX_RATE
    for r, h in RH:
        hand_by_rate[h][r] += 1
        rate_distribution[r] += 1

    rate_distribution = [0] + list(accumulate(rate_distribution))

    res = [[0] * 3 for _ in range(n)]
    for i in range(n):
        r, h = RH[i]
        win = rate_distribution[r]
        lose = rate_distribution[-1] - rate_distribution[r + 1]
        draw = hand_by_rate[h][r] - 1

        win += hand_by_rate[1][r] if h == 0 else hand_by_rate[2][r] if h == 1 else hand_by_rate[0][r]
        lose += hand_by_rate[2][r] if h == 0 else hand_by_rate[0][r] if h == 1 else hand_by_rate[1][r]

        res[i][0] = win
        res[i][1] = lose
        res[i][2] = draw

    for i in range(n):
        print(*res[i])


if __name__ == '__main__':
    resolve()
