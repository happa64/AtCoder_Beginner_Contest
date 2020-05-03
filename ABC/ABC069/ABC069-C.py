# https://atcoder.jp/contests/abc069/tasks/arc080_a
# C - 4-adjacent
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    # 2の倍数と4の倍数を数える
    cnt_2 = 0
    cnt_4 = 0
    for i in range(n):
        if A[i] % 4 == 0:
            cnt_4 += 1
        elif A[i] % 2 == 0:
            cnt_2 += 1

    # 4の倍数がn//2以上あればよく、また（2の倍数の数-1）分だけnが小さくなる
    if (n - max(0, cnt_2 - 1)) // 2 <= cnt_4:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    resolve()
