# https://atcoder.jp/contests/nikkei2019-qual/submissions/13677459
# B - Touitsu
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = input().rstrip()
    B = input().rstrip()
    C = input().rstrip()

    res = 0
    for a, b, c in zip(A, B, C):
        res += 1 if len(set(a + b + c)) == 2 else 2 if len(set(a + b + c)) == 3 else 0

    print(res)


if __name__ == '__main__':
    resolve()
