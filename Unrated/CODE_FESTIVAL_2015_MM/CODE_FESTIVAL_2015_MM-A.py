# https://atcoder.jp/contests/code-festival-2015-morning-middle/submissions/13146437
# A - ヘイホー君と最終試験
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k, m, r = map(int, input().split())
    S = sorted(list(int(input()) for _ in range(n - 1)), reverse=True)

    score = 0
    for i in range(n - 1 if n == k else k):
        score += S[i]

    if k * r <= score:
        print(0)
    else:
        if n != k:
            score -= S[k - 1]
        res = k * r - score
        print(max(0, res) if res <= m else -1)


if __name__ == '__main__':
    resolve()
