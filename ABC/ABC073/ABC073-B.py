# https://atcoder.jp/contests/abc073/submissions/13229247
# B - Theater
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    res = 0
    for i in range(n):
        l, r = map(int, input().split())
        res += r - l + 1

    print(res)


if __name__ == '__main__':
    resolve()
