# https://atcoder.jp/contests/abc043/submissions/13433935
# C - いっしょ
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要：
        aのとる範囲は-100～100であり、コストの総和が最小値になるには、yをこの範囲内にとる事が直感的にわかる。
        Nは高々100であり、yが取りうる数値の数も200であるため、yを全て試せば良い。

    計算量；O(N*200)
    :return:
    """
    n = int(input())
    A = list(map(int, input().split()))

    res = f_inf
    for y in range(-100, 101):
        cost = 0
        for i in range(n):
            cost += pow(abs(A[i] - y), 2)
        res = min(res, cost)
    print(res)


if __name__ == '__main__':
    resolve()
