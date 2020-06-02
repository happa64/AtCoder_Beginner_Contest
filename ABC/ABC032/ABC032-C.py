# https://atcoder.jp/contests/abc032/submissions/13940207
# C - 列
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    S = list(int(input()) for _ in range(n))

    if 0 in S:
        print(n)
        exit()

    if k == 0:
        print(0)
        exit()

    res = 0
    subs = deque([])
    ruiseki = 1
    for i in range(n):
        ruiseki *= S[i]
        subs.append(S[i])
        if ruiseki <= k:
            res = max(res, len(subs))
        else:
            while ruiseki > k:
                num = subs.popleft()
                ruiseki //= num
            res = max(res, len(subs))

    print(res)


if __name__ == '__main__':
    resolve()
