# https://atcoder.jp/contests/abc047/submissions/12868601
# D - 高橋君と見えざる手
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, t = map(int, input().split())
    A = list(map(int, input().split()))

    MAX_S = []
    max_s = 0
    for a in A[::-1]:
        if max_s < a:
            max_s = a
        MAX_S.append(max_s)
    MAX_S = MAX_S[::-1]

    cnt = defaultdict(int)
    for a, s in zip(A, MAX_S):
        cnt[s - a] += 1

    res = sorted(cnt.items(), reverse=True)
    print(res[0][1])


if __name__ == '__main__':
    resolve()
