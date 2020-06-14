# https://atcoder.jp/contests/code-festival-2016-qualc/submissions/14271793
# B - K個のケーキ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    k, t = map(int, input().split())
    A = list(map(int, input().split()))
    etc = sum(A) - max(A)
    res = max(0, max(A) - 1 - etc)
    print(res)


if __name__ == '__main__':
    resolve()
