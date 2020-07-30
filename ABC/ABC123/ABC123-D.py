# https://atcoder.jp/contests/abc123/submissions/15534002
# D - Cake 123
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    AB = []
    for i in range(X):
        for j in range(Y):
            AB.append(A[i] + B[j])
    AB.sort(reverse=True)

    res = []
    for i in range(min(K, len(AB))):
        for j in range(Z):
            res.append(AB[i] + C[j])
    res.sort(reverse=True)

    for i in range(K):
        print(res[i])


if __name__ == '__main__':
    resolve()
