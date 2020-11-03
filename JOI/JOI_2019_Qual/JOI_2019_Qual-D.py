# https://atcoder.jp/contests/joi2019yo/submissions/17859222
# D - 日本沈没 (Japan Sinks)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    B = sorted([[A[i], i + 1] for i in range(n)])

    res = 0
    cnt = 0
    X = [0] * (n + 2)
    while B:
        ma = -f_inf
        while B and (ma <= B[-1][0]):
            a, i = B.pop()
            ma = a
            if ma == 0:
                break
            X[i] = 1
            cnt += 1
            if X[i - 1]:
                cnt -= 1
            if X[i + 1]:
                cnt -= 1
        res = max(res, cnt)
    print(res)


if __name__ == '__main__':
    resolve()
