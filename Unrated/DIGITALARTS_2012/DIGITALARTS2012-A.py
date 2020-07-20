# https://atcoder.jp/contests/digitalarts2012/submissions/13451723
# A - C-Filter
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = list(input().split())
    n = int(input())

    for _ in range(n):
        t = input()
        if "*" not in t:
            for i in range(len(S)):
                if S[i] == t:
                    S[i] = "*" * len(t)
        else:
            for i in range(len(S)):
                if len(S[i]) == len(t):
                    for j in range(len(S[i])):
                        if t[j] != "*" and S[i][j] != t[j]:
                            break
                    else:
                        S[i] = "*" * len(t)

    print(" ".join(S))


if __name__ == '__main__':
    resolve()
