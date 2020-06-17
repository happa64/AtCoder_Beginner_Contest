# https://atcoder.jp/contests/arc012/submissions/14422989
# B - アキレスと亀
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N, va, vb, L = map(int, input().split())
    diff = L
    for _ in range(N):
        t = diff / va
        diff = t * vb

    print("{:.8f}".format(diff))


if __name__ == '__main__':
    resolve()
