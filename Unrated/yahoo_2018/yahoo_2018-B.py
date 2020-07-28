# https://atcoder.jp/contests/yahoo-procon2018-qual/submissions/15498077
# B - オークション
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, k = map(int, input().split())
    mi = 10 ** k
    start = (x // mi) * mi
    print(start + mi)


if __name__ == '__main__':
    resolve()
