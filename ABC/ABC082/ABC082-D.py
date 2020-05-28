# https://atcoder.jp/contests/abc082/submissions/13656007
# D - FT Robot
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    gx, gy = map(int, input().split())

    spl = list(map(len, s.split("T")))
    init_x = spl[0]
    is_x = 0
    to_x, to_y = [], []
    for i in range(1, len(spl)):
        if spl[i]:
            to_x.append(spl[i]) if is_x else to_y.append(spl[i])
        is_x ^= 1

    now_x = [init_x]
    for move in to_x:
        nx = set()
        for x in now_x:
            nx.add(x + move)
            nx.add(x - move)
        now_x = nx

    now_y = [0]
    for move in to_y:
        ny = set()
        for y in now_y:
            ny.add(y + move)
            ny.add(y - move)
        now_y = ny

    print("Yes" if gx in now_x and gy in now_y else "No")


if __name__ == '__main__':
    resolve()
