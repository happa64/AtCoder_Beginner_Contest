# https://atcoder.jp/contests/chokudai_S001/submissions/14660630
# G - あまり
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(input().split())
    print(int("".join(A)) % mod)


if __name__ == '__main__':
    resolve()
