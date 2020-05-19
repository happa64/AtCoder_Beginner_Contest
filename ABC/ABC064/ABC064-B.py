# https://atcoder.jp/contests/abc064/submissions/13399097
# B - Traveling AtCoDeer Problem
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要：
        最小の移動距離で全ての家にプレゼントを配るには、同じ家の間を往復しないような配り方をしなくてはならないです。
        これは、座標が小さい順に配る事で達成できます。
        つまり、aiをソートし、先頭と末尾の差をとった値が解となります。

    計算量；O(NlogN)
    :return:
    """
    n = int(input())
    A = sorted(list(map(int, input().split())))
    print(A[-1] - A[0])


if __name__ == '__main__':
    resolve()
