# https://atcoder.jp/contests/abc146/tasks/abc146_e
# E - Rem of Sum is Num
import sys
from itertools import accumulate
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = list(map(lambda x: int(x) - 1, input().split()))
    S = [0] + list(accumulate(A))
    S = [s % k for s in S]

    cnt = defaultdict(int)
    res = 0
    for i in range(n + 1):
        if i >= k:
            cnt[S[i - k]] -= 1
        res += cnt[S[i]]
        cnt[S[i]] += 1
    print(res)


if __name__ == '__main__':
    resolve()
