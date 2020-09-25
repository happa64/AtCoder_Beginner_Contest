# https://atcoder.jp/contests/joi2012ho/submissions/17002217
# A - JJOOII (JJOOII)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()

    prev = None
    cnt_j = cnt_o = cnt_i = 0
    res = 0
    for s in S:
        if prev is None:
            if s == "J":
                cnt_j += 1
                prev = "J"
        else:
            if s == "J":
                if prev == "J":
                    cnt_j += 1
                else:
                    cnt_j, cnt_o, cnt_i = 1, 0, 0
                    prev = "J"
            elif s == "O":
                if (prev == "J" and cnt_o == cnt_i == 0) or prev == "O":
                    cnt_o += 1
                    prev = "O"
                else:
                    cnt_j = cnt_o = cnt_i = 0
                    prev = None
            else:
                if (prev == "O" and cnt_i == 0) or prev == "I":
                    cnt_i += 1
                    prev = "I"
                else:
                    cnt_j = cnt_o = cnt_i = 0
                    prev = None
        if cnt_i and cnt_o <= cnt_j and cnt_o <= cnt_i:
            res = max(res, cnt_o)
    print(res)


if __name__ == '__main__':
    resolve()
