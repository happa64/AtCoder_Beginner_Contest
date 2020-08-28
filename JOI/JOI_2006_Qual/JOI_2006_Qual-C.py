# https://atcoder.jp/contests/joi2006yo/submissions/16278942
# C - JOI 2006 予選 問題3
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    T = 1
    E = 4
    W = 3
    N = 2
    S = 5
    B = 6
    res = 1
    for _ in range(n):
        s = input().rstrip()
        tmp_T = T
        tmp_W = W
        tmp_B = B
        tmp_E = E
        tmp_S = S
        tmp_N = N
        if s == "East":
            T = tmp_E
            W = tmp_T
            B = tmp_W
            E = tmp_B
        elif s == "North":
            T = tmp_N
            S = tmp_T
            N = tmp_B
            B = tmp_S
        elif s == "South":
            T = tmp_S
            S = tmp_B
            N = tmp_T
            B = tmp_N
        elif s == "West":
            T = tmp_W
            W = tmp_B
            B = tmp_E
            E = tmp_T
        elif s == "Left":
            N = tmp_E
            W = tmp_N
            S = tmp_W
            E = tmp_S
        else:
            N = tmp_W
            W = tmp_S
            S = tmp_E
            E = tmp_N
        res += T
    print(res)


if __name__ == '__main__':
    resolve()
