# https://atcoder.jp/contests/chokudai_S001/submissions/14661021
# F - 見える数
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    ma = A[0]
    res = 1
    for i in range(1, n):
        if A[i] > ma:
            ma = A[i]
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
