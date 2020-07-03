# https://atcoder.jp/contests/code-festival-2014-morning-easy/submissions/14914039
# A - 差の平均
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = 0
    for i in range(1, n):
        res += A[i] - A[i - 1]
    print(res / (n - 1))


if __name__ == '__main__':
    resolve()
