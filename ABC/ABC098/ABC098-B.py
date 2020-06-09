# https://atcoder.jp/contests/abc098/submissions/12926707
# B - Cut and Count
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input()

    # XとYを全探索する
    res = 0
    for i in range(n):
        X = set(s[:i])
        Y = set(s[i:])
        cnt = 0
        for x in X:
            if x in Y:
                cnt += 1
        res = max(res, cnt)

    print(res)


if __name__ == '__main__':
    resolve()
