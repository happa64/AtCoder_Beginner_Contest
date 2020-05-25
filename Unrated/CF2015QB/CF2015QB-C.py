# https://atcoder.jp/contests/code-festival-2015-qualb/submissions/13586318
# C - 旅館
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())), reverse=True)

    if n < m:
        print("NO")
        exit()

    for capa, num in zip(A, B):
        if capa < num:
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    resolve()
