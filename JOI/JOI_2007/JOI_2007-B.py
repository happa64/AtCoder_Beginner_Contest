# https://atcoder.jp/contests/joi2007ho/submissions/15253242
# B - 最長の階段
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = sorted(list(int(input()) for _ in range(k)))

    nums = [0] * (n + 1)
    for a in A:
        nums[a] = 1

    res = 0
    L = 0
    if nums[0] == 0:
        for i in range(1, n + 1):
            if nums[i] == 1:
                L += 1
            else:
                res = max(res, L)
                L = 0
        res = max(res, L)
    else:
        L_prev = 0
        for i in range(1, n + 1):
            if nums[i] == 1:
                L += 1
            else:
                res = max(res, L + L_prev + 1)
                L_prev = L
                L = 0
        res = max(res, L + L_prev + 1)
    print(res)


if __name__ == '__main__':
    resolve()
