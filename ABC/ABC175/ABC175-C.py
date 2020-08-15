# https://atcoder.jp/contests/abc175/submissions/15921891
# C - Walking Takahashi
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, k, d = map(int, input().split())
    cnt = abs(x) // d
    if cnt >= k:
        res = abs(x) - d * k
        print(res)
    else:
        now = abs(x) - cnt * d
        k -= cnt
        if k % 2 == 0:
            print(now)
        else:
            print(abs(now - d))


if __name__ == '__main__':
    resolve()
