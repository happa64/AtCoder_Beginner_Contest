# https://atcoder.jp/contests/typical90/submissions/22165734
# 027 - Sign Up Requests （★2）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    used = set()

    for i in range(1, n + 1):
        s = input().rstrip()
        if s not in used:
            used.add(s)
            print(i)


if __name__ == '__main__':
    solve()
