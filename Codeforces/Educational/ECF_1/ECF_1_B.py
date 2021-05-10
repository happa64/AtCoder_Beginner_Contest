# https://codeforces.com/contest/598/submission/99605351
# B - Queries on a String
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = list(input().rstrip())
    m = int(input())
    query = [list(map(int, input().split())) for _ in range(m)]

    for l, r, k in query:
        n = r - l + 1
        ss = S[l - 1:r]
        new_ss = [""] * n
        for i in range(n):
            new_ss[(i + k) % n] = ss[i]
        S[l - 1: r] = new_ss
    print("".join(S))


if __name__ == '__main__':
    resolve()
