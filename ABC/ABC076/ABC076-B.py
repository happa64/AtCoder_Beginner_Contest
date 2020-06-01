# https://atcoder.jp/contests/abc076/submissions/13925796
# B - Addition and Multiplication
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    k = int(input())

    res = 1
    for _ in range(n):
        if res < k:
            res *= 2
        else:
            res += k

    print(res)


if __name__ == '__main__':
    resolve()
