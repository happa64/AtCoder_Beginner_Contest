# https://atcoder.jp/contests/abc193/submissions/20540933
# D - Poker
import sys
from collections import defaultdict
from copy import deepcopy

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    K = int(input())
    T = input().rstrip()
    A = input().rstrip()

    rest = defaultdict(int)
    for i in range(1, 10):
        rest[i] = K

    t_cnt = defaultdict(int)
    a_cnt = defaultdict(int)
    for num1, num2 in zip(T[:4], A[:4]):
        rest[int(num1)] -= 1
        t_cnt[int(num1)] += 1
        rest[int(num2)] -= 1
        a_cnt[int(num2)] += 1

    win = 0
    tot = 0
    for k1, v1 in rest.items():
        if v1 == 0:
            continue
        rest[k1] -= 1
        t_cnt[k1] += 1
        t_score = sum(i * pow(10, t_cnt[i]) for i in range(1, 10))
        for k2, v2 in rest.items():
            if v2 == 0:
                continue
            a_cnt[k2] += 1
            a_score = sum(i * pow(10, a_cnt[i]) for i in range(1, 10))
            a_cnt[k2] -= 1
            if t_score > a_score:
                win += v1 * v2
            tot += v1 * v2
        rest[k1] += 1
        t_cnt[k1] -= 1

    res = win / tot
    print(res)


if __name__ == '__main__':
    resolve()
