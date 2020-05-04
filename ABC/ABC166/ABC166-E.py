# https://atcoder.jp/contests/abc166/tasks/abc166_e
# E - This Message Will Self-Destruct in 5s
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    # j - i = A[i] + A[j]を変形すると、A[i] + i = j - A[j]となり、これをLi = Rjと置く
    # LiとRjを全て計算し、それぞれ配列に入れる
    L = [0] * n
    R = [0] * n
    for i in range(n):
        L[i] = i + 1 + A[i]
        R[i] = i + 1 - A[i]


    DL = Counter(L)
    DR = Counter(R)

    res = 0
    # LiとRjのkeyが一致する場合、valueを掛け合わせた値の総和が解となる
    for k, v in DL.items():
        if DR.get(k, 0) != 0:
            res += DR.get(k) * v
        else:
            DR[k] = v

    print(res)


if __name__ == '__main__':
    resolve()
