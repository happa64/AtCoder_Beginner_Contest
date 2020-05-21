# https://atcoder.jp/contests/abc014/submissions/13452162
# B - 価格の合計
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))[::-1]
    bit = bin(x)[2:].zfill(n)

    res = 0
    for idx, flg in enumerate(bit):
        if int(flg):
            res += A[idx]

    print(res)


if __name__ == '__main__':
    resolve()
