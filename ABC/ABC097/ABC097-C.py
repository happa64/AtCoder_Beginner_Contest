# https://atcoder.jp/contests/arc097/submissions/14694811
# C - K-th Substring
import sys
from heapq import heapify, heappop

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    k = int(input())
    n = len(S)

    SS = set()
    for i in range(n):
        ss = S[i]
        SS.add(ss)
        for j in range(i + 1, min(n, i + k)):
            ss += S[j]
            SS.add(ss)

    SS = list(SS)
    heapify(SS)
    for _ in range(k):
        res = heappop(SS)
    print(res)


if __name__ == '__main__':
    resolve()
