# https://atcoder.jp/contests/joi2016ho/submissions/18968420
# B - スタンプラリー ２ (Collecting Stamps 2)
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = input()

    cnt = [[0] * n for _ in range(3)]
    for i in range(n):
        if S[i] == "J":
            cnt[0][i] = 1
        elif S[i] == "O":
            cnt[1][i] = 1
        else:
            cnt[2][i] = 1

    cnt_joi = [[0] * (n + 1) for _ in range(3)]
    for i in range(3):
        cnt_joi[i] = [0] + list(accumulate(cnt[i]))

    cnt_o_r = [0] * (n + 1)
    tmp = 0
    for i in reversed(range(n)):
        if S[i] == "O":
            tmp += cnt_joi[2][-1] - cnt_joi[2][i + 1]
        cnt_o_r[i] = tmp

    cnt_o_i = [0] * (n + 1)
    tmp = 0
    for i in range(n):
        if S[i] == "O":
            tmp += cnt_joi[0][i + 1]
        cnt_o_i[i + 1] = tmp

    init = 0
    for i in range(n):
        if S[i] == "O":
            left_j = cnt_joi[0][i + 1]
            right_i = cnt_joi[2][-1] - cnt_joi[2][i + 1]
            init += left_j * right_i

    res = init
    for i in range(n + 1):
        res = max(res, init + cnt_o_r[i])
        left_j = cnt_joi[0][i]
        right_i = cnt_joi[2][-1] - cnt_joi[2][i]
        res = max(res, init + left_j * right_i)
        res = max(res, init + cnt_o_i[i])
    print(res)



if __name__ == '__main__':
    resolve()
