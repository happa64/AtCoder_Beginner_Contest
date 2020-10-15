# https://atcoder.jp/contests/abc083/submissions/17407413
# D - Wide Flip
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = ["-1"] + list(input().rstrip())
    n = len(S)
    kouho = []
    for i in range(1, n):
        if S[i] != S[i - 1]:
            kouho.append(max(i - 1, n - i))
    res = min(kouho)
    print(res)


if __name__ == '__main__':
    resolve()
