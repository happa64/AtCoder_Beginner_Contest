# https://atcoder.jp/contests/joisc2011/submissions/19042342
# ioi - 国際情報オリンピック (IOI)
import sys
from bisect import bisect_right

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def calc(x, y):
        idx = bisect_right(Q, x)
        return k - idx - 1 if y > x else k - idx

    k, n, m = map(int, input().split())
    P = list(int(input()) for _ in range(k))
    Q = sorted(P)
    v = 100 * (n - m)
    l = (k + 11) // 12 - 1

    res = [0] * k
    for i in range(k):
        if calc(P[i] - v, P[i]) <= l:
            res[i] = 2
        else:
            if calc(P[i] + v, P[i]) <= l:
                res[i] = 1

    for i in range(k):
        if res[i] == 2:
            print(i + 1)
    print("--------")
    for i in range(k):
        if res[i] >= 1:
            print(i + 1)


if __name__ == '__main__':
    resolve()
