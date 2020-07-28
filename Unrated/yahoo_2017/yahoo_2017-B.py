# https://atcoder.jp/contests/yahoo-procon2017-qual/submissions/15498109
# B - オークション
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = sorted(list(map(int, input().split())))

    dec = 0
    res = 0
    for i in range(k):
        res += A[i] + dec
        dec += 1
    print(res)


if __name__ == '__main__':
    resolve()
