# https://atcoder.jp/contests/abc149/submissions/13954998
# D - Prediction and Restriction
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = list(input())

    res = 0
    for i in range(n):
        if i < k:
            res += p if t[i] == "r" else r if t[i] == "s" else s
        else:
            if t[i - k] != t[i]:
                res += p if t[i] == "r" else r if t[i] == "s" else s
            else:
                t[i] = "e"

    print(res)


if __name__ == '__main__':
    resolve()
