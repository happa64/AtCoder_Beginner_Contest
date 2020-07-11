# https://atcoder.jp/contests/aising2020/submissions/15144901
# B - An Odd Problem
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = 0
    for i in range(n):
        if i % 2 == 0 and A[i] % 2 != 0:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
