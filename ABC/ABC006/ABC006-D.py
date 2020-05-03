# https://atcoder.jp/contests/abc006/tasks/abc006_3
# C - スフィンクスのなぞなぞ
import bisect
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    C = list(int(input()) for _ in range(n))

    # 抜き取った後のに増加列が最長になるパターンが答えとなる
    # 最長増加部分列(LIS)の長さを二分探索にて求める
    LIS = [C[0]]
    for i in range(n):
        if C[i] > LIS[-1]:
            LIS.append(C[i])
        else:
            idx = bisect.bisect_left(LIS, C[i])
            LIS[idx] = C[i]

    print(n - len(LIS))


if __name__ == '__main__':
    resolve()
