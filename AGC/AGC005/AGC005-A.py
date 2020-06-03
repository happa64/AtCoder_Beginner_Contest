# https://atcoder.jp/contests/agc005/tasks/agc005_a
# A - STring
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve1():
    x = input()

    cnt_S = 0
    cnt_T = 0
    res = 0
    i = 0
    while i < len(x):
        if x[i] == "S":
            cnt_S += 1
            i += 1

        elif x[i] == "T" and cnt_S != 0:
            while i < len(x) and x[i] == "T":
                cnt_T += 1
                i += 1
            res += min(cnt_S, cnt_T) * 2
            cnt_S -= min(cnt_S, cnt_T)
            cnt_T = 0
        else:
            i += 1

    print(len(x) - res)


def resolve2():
    x = input()
    n = len(x)

    stack = 0
    res = 0
    for i in range(n):
        if x[i] == "S":
            stack += 1
        elif stack > 0:
            stack -= 1
            res += 1

    print(n - res * 2)


if __name__ == '__main__':
    resolve2()
