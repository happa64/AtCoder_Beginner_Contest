# https://atcoder.jp/contests/abc170/submissions/14378482
# D - Not Divisible
import sys
from collections import Counter
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = sorted(list(map(int, input().split())))
    D = Counter(A)

    dup = set()
    for k, v in D.items():
        if v > 1:
            dup.add(k)

    judge = [False] * (A[-1] + 1)
    res = 0
    for a in A:
        if judge[a]:
            continue
        else:
            if a not in dup:
                res += 1
            for i in range(a, A[-1] + 1, a):
                judge[i] = True

    print(res)


if __name__ == '__main__':
    resolve()
