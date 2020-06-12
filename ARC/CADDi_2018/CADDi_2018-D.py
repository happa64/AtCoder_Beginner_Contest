# https://atcoder.jp/contests/caddi2018/submissions/14186934
# D - Harlequin
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(int(input()) for _ in range(n))

    for a in A:
        if a % 2 != 0:
            print("first")
            break
    else:
        print("second")


if __name__ == '__main__':
    resolve()
