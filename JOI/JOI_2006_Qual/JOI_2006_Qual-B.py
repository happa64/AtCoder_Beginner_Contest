# https://atcoder.jp/contests/joi2006yo/submissions/16278045
# B - JOI 2006 予選 問題2
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    D = {}
    for _ in range(n):
        a, b = input().split()
        D[a] = b

    res = ""
    m = int(input())
    for _ in range(m):
        s = input().rstrip()
        if D.get(s) is not None:
            res += D[s]
        else:
            res += s
    print(res)


if __name__ == '__main__':
    resolve()
