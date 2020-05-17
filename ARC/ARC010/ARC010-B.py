# https://atcoder.jp/contests/arc010/submissions/13287743
# B - 超大型連休
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    MD = list(map(int, input().split("/")) for _ in range(n))
    calender = set()

    # 休日リストの作成
    amari = 0
    for i in range(1, 12 + 1):
        k = 29 if i == 2 else 30 if i == 4 or i == 6 or i == 9 or i == 11 else 31
        for j in range(1, k + 1):
            if (j + amari) % 7 == 1 or (j + amari) % 7 == 0:
                calender.add((i, j))
        amari = (k + amari) % 7

    # 祝日の追加
    for i in range(n):
        m, d = MD[i]
        while (m, d) in calender:
            k = 29 if m == 2 else 30 if m == 4 or m == 6 or m == 9 or m == 11 else 31
            if d + 1 > k:
                if m + 1 <= 12:
                    m += 1
                    d = 1
                else:
                    break
            else:
                d += 1
        else:
            calender.add((m, d))

    calender = sorted(calender, key=lambda x: (x[0], x[1]))

    res = 0
    cnt = 1
    # 連続する休日のカウント及び最大値を見つける
    for i in range(len(calender) - 1):
        if calender[i][0] == calender[i + 1][0]:
            if calender[i][1] + 1 == calender[i + 1][1]:
                cnt += 1
                res = max(res, cnt)
            else:
                res = max(res, cnt)
                cnt = 1
        else:
            m = calender[i][0]
            k = 29 if m == 2 else 30 if m == 4 or m == 6 or m == 9 or m == 11 else 31
            if calender[i][1] == k and calender[i + 1][1] == 1:
                cnt += 1
                res = max(res, cnt)
            else:
                res = max(res, cnt)
                cnt = 1

    print(res)


if __name__ == '__main__':
    resolve()
