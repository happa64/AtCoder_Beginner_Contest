# https://atcoder.jp/contests/joi2008ho/submissions/16257909
# B - 共通部分文字列
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    T = input()
    n = len(S)

    res = 0
    left = right = 0
    while left < n and right < n:
        ss = S[left: right + 1]
        if ss in T:
            res = max(res, right - left + 1)
            right += 1
        else:
            left += 1
            right = max(right, left)
    print(res)


if __name__ == '__main__':
    resolve()
