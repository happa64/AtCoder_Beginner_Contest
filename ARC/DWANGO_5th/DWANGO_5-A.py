# https://atcoder.jp/contests/dwacon5th-prelims/submissions/13654680
# A - Thumbnail
import sys
import statistics

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    ave = statistics.mean(A)

    diff = f_inf
    res = 0
    for i in range(n):
        if diff > abs(A[i] - ave):
            res = i
            diff = abs(A[i] - ave)

    print(res)


if __name__ == '__main__':
    resolve()
