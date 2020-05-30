# https://atcoder.jp/contests/exawizards2019/submissions/13700533
# A - Regular Triangle
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())
    print("Yes" if a == b == c else "No")


if __name__ == '__main__':
    resolve()
