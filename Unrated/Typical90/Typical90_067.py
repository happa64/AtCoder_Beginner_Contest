# https://atcoder.jp/contests/typical90/submissions/23494076
# 067 - Base 8 to 9（★2）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def trans_decimal(X):
    X = str(X)[::-1]
    res = 0
    for i, x in enumerate(X):
        res += pow(8, i) * int(x)
    return res


def trans_nine(x):
    res = ""
    while x:
        x, r = divmod(x, 9)
        if r == 8:
            r = 5
        res += str(r)
    return int(res[::-1])


def solve():
    n, k = map(int, input().split())
    if n == 0:
        print(0)
        exit()
    for _ in range(k):
        n = trans_decimal(n)
        n = trans_nine(n)
    print(n)


if __name__ == '__main__':
    solve()
