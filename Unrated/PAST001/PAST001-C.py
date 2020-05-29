# https://atcoder.jp/contests/past201912-open/tasks/past201912_c
# C - 3 番目
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    L = sorted(list(map(int, input().split())), reverse=True)
    print(L[2])


if __name__ == '__main__':
    resolve()
