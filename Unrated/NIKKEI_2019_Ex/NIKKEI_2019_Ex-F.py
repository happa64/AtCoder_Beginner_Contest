# https://atcoder.jp/contests/nikkei2019-ex/submissions/17101133
# F - コラッツ問題
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    P = int(input())
    if P == 0:
        print(10 ** 16)
        exit()
    x = 1789997546303
    res = [0] * 1000
    idx = 0
    while x != 1:
        res[idx] = x
        if x % 2 == 0:
            x //= 2
        else:
            x = x * 3 + 1
        idx += 1
    res = res[::-1]
    print(res[P - 1])


if __name__ == '__main__':
    resolve()
