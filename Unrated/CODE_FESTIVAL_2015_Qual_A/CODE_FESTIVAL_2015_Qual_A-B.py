# https://atcoder.jp/contests/code-festival-2015-quala/submissions/14843194
# B - とても長い数列
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
        res = res * 2 + A[i]
    print(res)


if __name__ == '__main__':
    resolve()
