# https://atcoder.jp/contests/ddcc2019-final/submissions/17099227
# A - レース (Race)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = list(input())

    ma = 0
    cnt = 0
    for i in range(n):
        if s[i] == ">":
            cnt += 1
            ma = max(ma, cnt)
        else:
            cnt = 0
    if ma == 0:
        s[0] = ">"

    res = 0
    cnt = 0
    flg = True
    for i in range(n):
        if s[i] == "-":
            res += 1
            cnt = 0
        else:
            res += (1 / (cnt + 2))
            cnt += 1
            if cnt == ma and flg:
                s[i + 1] = ">"
                flg = False
    print(res)


if __name__ == '__main__':
    resolve()
