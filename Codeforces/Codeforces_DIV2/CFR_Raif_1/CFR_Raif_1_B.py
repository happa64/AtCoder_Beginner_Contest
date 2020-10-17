# https://codeforces.com/contest/1428/submission/95765327
# B. Belted Rooms
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        S = list(input().rstrip())
        if "<" in set(S) and ">" in set(S):
            res = [False] * n
            for i in range(n):
                if S[i] == "-":
                    res[i] = True
                    res[(i + 1) % n] = True
            print(res.count(True))
        else:
            print(n)


if __name__ == '__main__':
    resolve()
