# https://atcoder.jp/contests/abc003/tasks/abc003_3
# C - AtCoderプログラミング講座
import sys

sys.setrecursionlimit(10 ** 7)


def resolve():
    n, k = map(int, input().split())
    R = list(map(int, input().split()))
    R.sort()

    rate = 0
    for i in R[n - k: n]:
        rate = (rate + i) / 2
    print(rate)


if __name__ == '__main__':
    resolve()
