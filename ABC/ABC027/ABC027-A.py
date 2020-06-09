# https://atcoder.jp/contests/abc027/submissions/14127257
# A - 長方形
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    l1, l2, l3 = map(int, input().split())
    if l1 == l2 == l3:
        print(l1)
    elif l1 == l2:
        print(l3)
    elif l1 == l3:
        print(l2)
    elif l2 == l3:
        print(l1)


if __name__ == '__main__':
    resolve()
