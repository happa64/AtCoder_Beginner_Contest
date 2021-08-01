# https://atcoder.jp/contests/abc210/submissions/24281309
# B - Bouzu Mekuri
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    S = input().rstrip()

    for i in range(n):
        if i % 2 == 0 and S[i] == "1":
            print("Takahashi")
            break
        elif i % 2 == 1 and S[i] == "1":
            print("Aoki")
            break


if __name__ == '__main__':
    solve()
