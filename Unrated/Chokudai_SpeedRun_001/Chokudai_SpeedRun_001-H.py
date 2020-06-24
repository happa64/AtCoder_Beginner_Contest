# https://atcoder.jp/contests/chokudai_S001/submissions/14660699
# H - LIS
import sys
import bisect
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    L = list(map(int, input().split()))

    LIS = [L[0]]
    for i in range(n):
        if L[i] > LIS[-1]:
            LIS.append(L[i])
        else:
            idx = bisect.bisect_left(LIS, L[i])
            LIS[idx] = L[i]

    print(len(LIS))


if __name__ == '__main__':
    resolve()
