# https://atcoder.jp/contests/abc027/submissions/13477026
# B - 島と橋
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    # 平均値が整数でなければ解は存在しない
    if sum(A) % n != 0:
        print(-1)
        exit()

    # 最終的な島の住民の平均人数
    ave = sum(A) // n

    # 架ける橋
    edge = [0 for _ in range(n - 1)]

    for i in range(n):
        # 島の住民が平均より多ければ、平均より少ない島に移動させる
        if A[i] > ave:
            j = i
            while A[j] >= ave:
                j += 1
                edge[j - 1] = 1
            diff = A[i] - ave
            A[i] -= diff
            A[j] += diff
        # 島の住民が平均より少なければ、平均より多い島から移動させる
        elif A[i] < ave:
            j = i
            while A[j] <= ave:
                j += 1
                edge[j - 1] = 1
            diff = ave - A[i]
            A[i] += diff
            A[j] -= diff

    print(sum(edge))


if __name__ == '__main__':
    resolve()
