# https://atcoder.jp/contests/joi2009yo/submissions/15251743
# B - コンテスト
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    W = sorted(list(int(input()) for _ in range(10)), reverse=True)
    K = sorted(list(int(input()) for _ in range(10)), reverse=True)
    W_score = sum(W[:3])
    K_score = sum(K[:3])
    print(W_score, K_score)


if __name__ == '__main__':
    resolve()
