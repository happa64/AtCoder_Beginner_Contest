# https://atcoder.jp/contests/past202012-open/submissions/19042577
# A - ○✕ゲーム
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()

    cnt_o = cnt_x = 0
    for s in S:
        if s == "o":
            cnt_o += 1
            cnt_x = 0
        else:
            cnt_o = 0
            cnt_x += 1

        if cnt_o == 3:
            print("o")
            break

        if cnt_x == 3:
            print("x")
            break
    else:
        print("draw")


if __name__ == '__main__':
    resolve()
