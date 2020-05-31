# https://atcoder.jp/contests/nomura2020/submissions/13716422
# A - Study Scheduling
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    h1, m1, h2, m2, k = map(int, input().split())
    t = (h2 - h1) * 60 + (m2 - m1)
    print(max(0, t - k))


if __name__ == '__main__':
    resolve()
