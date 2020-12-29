# https://atcoder.jp/contests/joi2020ho/submissions/19039118
# B - JJOOII 2 (JJOOII 2)
import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    S = list(input())

    j, o, i = [], [], []
    for idx in range(n):
        if S[idx] == "J":
            j.append(idx)
        elif S[idx] == "O":
            o.append(idx)
        else:
            i.append(idx)

    res = f_inf
    for idx in range(len(j) - k + 1):
        left_j = j[idx]
        if idx + k - 1 < len(j):
            right_j = j[idx + k - 1]
            idx = bisect_left(o, right_j)
            if idx + k - 1 < len(o):
                right_o = o[idx + k - 1]
                idx = bisect_left(i, right_o)
                if idx + k - 1 < len(i):
                    right_i = i[idx + k - 1]
                    t = right_i - left_j + 1 - k * 3
                    res = min(res, t)
    print(res if res != f_inf else -1)


if __name__ == '__main__':
    resolve()
