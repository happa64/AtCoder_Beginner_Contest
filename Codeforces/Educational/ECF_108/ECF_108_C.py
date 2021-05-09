# https://codeforces.com/contest/1519/submission/115770488
# C - Berland Regional
import sys
from collections import defaultdict
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    U = list(map(int, input().split()))
    S = list(map(int, input().split()))

    belong_dict = defaultdict(list)
    for u, s in zip(U, S):
        belong_dict[u].append(s)

    belong_tmp = [[len(v), v] for v in belong_dict.values()]
    belong_tmp.sort()
    belong = [[0] + list(accumulate(sorted(v))) for _, v in belong_tmp]

    init = sum(S)
    pos = 0
    res = [0] * n
    for k in range(1, n + 1):
        tmp = init
        for i in range(pos, len(belong)):
            if (len(belong[i]) - 1) < k:
                pos = i + 1
                init -= belong[i][-1]
            rem = (len(belong[i]) - 1) % k
            tmp -= belong[i][rem]
        res[k - 1] = tmp
    print(*res)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
