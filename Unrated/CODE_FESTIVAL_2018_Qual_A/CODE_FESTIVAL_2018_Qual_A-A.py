# https://atcoder.jp/contests/code-festival-2018-quala/submissions/15390161
# A - 配点
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A = int(input())
    B = int(input())
    C = int(input())
    S = int(input())
    for a in [A, A + 1]:
        for b in [B, B + 1]:
            for c in [C, C + 1]:
                if a + b + c == S:
                    print("Yes")
                    exit()
    print("No")


if __name__ == '__main__':
    resolve()
