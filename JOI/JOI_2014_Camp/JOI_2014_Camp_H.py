# https://atcoder.jp/contests/joisc2014/submissions/19028929
# H - JOIOJI
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = input()

    P = [0] * (n + 1)
    Q = [0] * (n + 1)
    cnt_j = cnt_o = cnt_i = 0
    for i in range(n):
        if S[i] == "J":
            cnt_j += 1
        elif S[i] == "O":
            cnt_o += 1
        else:
            cnt_i += 1
        P[i + 1] = cnt_o - cnt_j
        Q[i + 1] = cnt_i - cnt_j

    D = defaultdict(list)
    for i in range(n + 1):
        D[(P[i], Q[i])].append(i)

    res = 0
    for v in D.values():
        ma = max(v)
        mi = min(v)
        res = max(res, ma - mi)
    print(res)


if __name__ == '__main__':
    resolve()
