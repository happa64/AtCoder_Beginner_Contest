# https://atcoder.jp/contests/code-formula-2014-quala/submissions/14799926
# A - 立方数
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A = int(input())
    for i in range(1, 1000):
        if pow(i, 3) == A:
            print("YES")
            break
    else:
        print("NO")


if __name__ == '__main__':
    resolve()
