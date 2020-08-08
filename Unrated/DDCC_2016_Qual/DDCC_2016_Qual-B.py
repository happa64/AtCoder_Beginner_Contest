# https://atcoder.jp/contests/ddcc2016-qual/submissions/15761565
# B - ステップカット
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def calc(x):
        if 0 < x < n:
            return 2 * pow(r ** 2 - (r - 2 * r / n * x) ** 2, 0.5)
        else:
            return 0

    r, n, m = map(int, input().split())

    res = 0
    for i in range(1, n + m):
        res += max(calc(i), calc(i - m))
    print(res)


if __name__ == '__main__':
    resolve()
