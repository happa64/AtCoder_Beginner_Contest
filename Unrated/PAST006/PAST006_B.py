# https://atcoder.jp/contests/past202104-open/submissions/22052085
# B - PASTal Code
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    S = input()
    n = len(S)

    res = "none"
    for i in range(0, n, 4):
        s = S[i: i + 4]
        if s == "post":
            res = i // 4 + 1
            break
    print(res)


if __name__ == '__main__':
    solve()
