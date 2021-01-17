# https://atcoder.jp/contests/keyence2021/submissions/19463330
# A - Two Sequences 2
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    C = [-1]
    prev = -1
    for i in range(n):
        a = A[i]
        b = B[i]
        if prev < a:
            C.append(max(C[-1], prev * b, a * b))
            prev = a
        else:
            C.append(max(C[-1], prev * b))
    print(*C[1:], sep="\n")


if __name__ == '__main__':
    resolve()
