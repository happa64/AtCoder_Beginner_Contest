# https://atcoder.jp/contests/abc194/submissions/20695130
# B - Job Assignment
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    AB = [list(map(int, input().split())) for _ in range(n)]

    res = f_inf
    for i in range(n):
        for j in range(n):
            if i == j:
                res = min(res, sum(AB[i]))
            else:
                a = AB[i][0]
                b = AB[j][1]
                res = min(res, max(a, b))
    print(res)


if __name__ == '__main__':
    solve()
