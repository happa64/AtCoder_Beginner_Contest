# https://atcoder.jp/contests/abc018/submissions/14080028
#A - 豆まき
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A = int(input())
    B = int(input())
    C = int(input())

    res = []
    if A > B > C:
        res = [1, 2, 3]
    elif A > C > B:
        res = [1, 3, 2]
    elif B > A > C:
        res = [2, 1, 3]
    elif B > C > A:
        res = [3, 1, 2]
    elif C > A > B:
        res = [2, 3, 1]
    elif C > B > A:
        res = [3, 2, 1]
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
