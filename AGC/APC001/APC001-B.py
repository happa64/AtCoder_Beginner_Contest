# https://atcoder.jp/contests/apc001/tasks/apc001_b
# B - Two Arrays
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    # bをaにするための操作回数をカウントし、bをaに合わせる
    for i in range(n):
        if B[i] < A[i]:
            cnt += A[i] - B[i]
            B[i] = A[i]

    # bをaにするための操作回数を上記のカウントから引いていく
    # 差が奇数の場合、操作回数は切り捨てでなければ、sum(A) > sum(B)となってしまうため注意
    for i in range(n):
        if B[i] > A[i]:
            cnt -= (B[i] - A[i]) // 2

    # bに足す回数よりaに足す回数の方が大きければ一致させられる
    if cnt <= 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    resolve()
