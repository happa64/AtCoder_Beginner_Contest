# https://atcoder.jp/contests/abc060/submissions/14267065
# A - Shiritori
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A, B, C = input().split()
    if A[-1] == B[0] and B[-1] == C[0]:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    resolve()
