# https://atcoder.jp/contests/abc008/tasks/abc008_3
# C - コイン
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    C = list(int(input()) for _ in range(n))

    res = 0
    # 表を向いているコインの枚数の期待値 = 各コインが表を向く確率の総和
    # まず各コインの約数の数（cnt）を調べる
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i != j:
                if C[i] % C[j] == 0:
                    cnt += 1
        # 約数がコインの左側に偶数枚あれば、表を向いていることになる
        # 左側に偶数枚ある場合の数は、cntが偶数の場合：cnt // 2 + 1、奇数の場合、(cnt + 1) // 2
        # 表を向いている確率は、cntが偶数の場合：(cnt // 2 + 1) // (cnt + 1) = (cnt + 2) // (2 * cnt + 2)
        # cntが奇数の場合：((cnt + 1) // 2) // (cnt + 1) = 1 / 2
        if cnt % 2 == 0:
            res += (cnt + 2) / (2 * cnt + 2)
        else:
            res += 1 / 2
    print(res)


if __name__ == '__main__':
    resolve()
