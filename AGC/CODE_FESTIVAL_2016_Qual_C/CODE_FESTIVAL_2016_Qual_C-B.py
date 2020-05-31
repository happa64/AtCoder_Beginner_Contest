# https://atcoder.jp/contests/code-festival-2016-qualc/tasks/codefestival_2016_qualC_b
# B - K個のケーキ
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    k, t = map(int, input().split())
    A = list(map(int, input().split()))

    # ケーキの種類iとケーキの個数aiの配列を作り、ケーキの個数順に昇順ソートする
    B = []
    for i in range(t):
        B.append([i + 1, A[i]])
    B = sorted(B, key=lambda x: x[1])

    # ケーキの種類が1つしかなければ、日にち-1が答え
    if t == 1:
        print(k - 1)
        exit()

    res = 0
    # pre：前回食べたケーキ
    pre = 0
    for i in range(k):
        # 一番多いケーキが前回食べたケーキでなければ、一番多いケーキを食べる
        if pre != B[-1][0]:
            pre = B[-1][0]
            B[-1][1] -= 1
            B = sorted(B, key=lambda x: x[1])
        else:
            # 前回食べたケーキが一番多いケーキであれば、二番目に多いケーキを食べる
            if B[-2][1] != 0:
                pre = B[-2][0]
                B[-2][1] -= 1
                B = sorted(B, key=lambda x: x[1])

            # 前回食べたケーキが一番多いケーキであり、二番目に多いケーキがもうなければ、前回食べたケーキを食べる
            else:
                B[-1][1] -= 1
                res += 1

    print(res)


if __name__ == '__main__':
    resolve()
