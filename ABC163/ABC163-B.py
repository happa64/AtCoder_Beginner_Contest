# https://atcoder.jp/contests/abc163/tasks/abc163_b
# B - Homework
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    if  n >= sum(A):
        print(n - sum(A))
    else:
        print(-1)

if __name__ == '__main__':
    resolve()
