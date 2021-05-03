# https://atcoder.jp/contests/typical90/submissions/21931691
# 010 - Score Sum Queries（★2）
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    class1 = [0] * n
    class2 = [0] * n
    for i in range(n):
        c, p = map(int, input().split())
        if c == 1:
            class1[i] = p
        else:
            class2[i] = p
    class1_acc = [0] + list(accumulate(class1))
    class2_acc = [0] + list(accumulate(class2))
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        print(class1_acc[r] - class1_acc[l - 1], class2_acc[r] - class2_acc[l - 1])


if __name__ == '__main__':
    solve()
