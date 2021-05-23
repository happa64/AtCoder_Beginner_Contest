# https://atcoder.jp/contests/abc202/submissions/22796922
# B - 180°
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    s = list(input().rstrip())
    n = len(s)

    for i in range(n):
        if s[i] == "6":
            s[i] = "9"
        elif s[i] == "9":
            s[i] = "6"

    res = "".join(s[::-1])
    print(res)


if __name__ == '__main__':
    solve()
