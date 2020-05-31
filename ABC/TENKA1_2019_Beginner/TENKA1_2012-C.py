# https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_c
# C - Stones
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = input()
    White = [0] * (n + 1)
    Black = [0] * (n + 1)

    # 左側を全部白にする場合、変更する必要のある石の個数
    for i in range(n):
        if S[i] == "#":
            Black[i + 1] = Black[i] + 1
        else:
            Black[i + 1] = Black[i]

    # 右側を全部黒にする場合、変更する必要のある石の個数
    for i in reversed(range(n)):
        if S[i] == ".":
            White[i] = White[i + 1] + 1
        else:
            White[i] = White[i + 1]

    res = f_inf
    # 左側を全部白に、右側を全部黒にする場合、変更する必要のある石の個数の最小値
    for i in range(n + 1):
        res = min(res, White[i] + Black[i])

    print(res)


if __name__ == '__main__':
    resolve()

