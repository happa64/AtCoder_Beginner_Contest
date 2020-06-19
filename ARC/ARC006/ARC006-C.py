# https://atcoder.jp/contests/arc006/submissions/14464623
# C - 積み重ね
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    W = list(int(input()) for _ in range(n))
    B = [W[0]]
    for i in range(1, n):
        B.sort()
        for j in range(len(B)):
            if W[i] <= B[j]:
                B[j] = W[i]
                break
        else:
            B.append(W[i])
    print(len(B))


if __name__ == '__main__':
    resolve()
