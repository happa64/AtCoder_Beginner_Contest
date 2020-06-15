# https://atcoder.jp/contests/tenka1-2015-qualb/submissions/14384976
# A - 天下一プログラマーコンテスト1998
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A = [0] * 20
    A[0] = 100
    A[1] = 100
    A[2] = 200
    for i in range(3, 20):
        A[i] = A[i - 1] + A[i - 2] + A[i - 3]
    print(A[-1])


if __name__ == '__main__':
    resolve()
