# https://atcoder.jp/contests/joi2009yo/submissions/15251689
# A - タイムカード
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    ABC = [list(map(int, input().split())) for _ in range(3)]

    for i in range(3):
        h1, m1, s1, h2, m2, s2 = ABC[i]
        diff = (h2 * 3600 + m2 * 60 + s2) - (h1 * 3600 + m1 * 60 + s1)
        H, M = divmod(diff, 3600)
        M, S = divmod(M, 60)
        print(H, M, S)


if __name__ == '__main__':
    resolve()
