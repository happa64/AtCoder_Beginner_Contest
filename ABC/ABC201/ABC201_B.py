# https://atcoder.jp/contests/abc201/submissions/22599646
# B - Do you know the second highest mountain?
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    ST = []
    for _ in range(n):
        s, t = input().split()
        ST.append((int(t), s))
    ST.sort(reverse=True)

    res = ST[1][1]
    print(res)


if __name__ == '__main__':
    solve()
