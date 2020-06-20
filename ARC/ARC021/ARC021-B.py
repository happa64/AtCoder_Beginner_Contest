# https://atcoder.jp/contests/arc021/submissions/14493262
# B - Your Numbers are XORed...
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    L = int(input())
    B = list(int(input()) for _ in range(L))
    A = [0]

    for i in range(1, L):
        A.append(A[i - 1] ^ B[i - 1])

    if A[0] ^ A[-1] != B[-1]:
        print(-1)
    else:
        print(*A, sep="\n")


if __name__ == '__main__':
    resolve()
