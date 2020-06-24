# https://atcoder.jp/contests/abc112/submissions/14652036
# C - Pyramid
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    XYH = [list(map(int, input().split())) for _ in range(n)]

    info = []
    for x, y, h in XYH:
        if h == 0:
            continue
        info.append([x, y, h])

    if len(info) == 1:
        print(*info[0])
        exit()

    for Cx in range(100 + 1):
        for Cy in range(100 + 1):
            tmp = set()
            for x, y, h in info:
                if h == 0:
                    continue
                H = h + abs(x - Cx) + abs(y - Cy)
                tmp.add(H)
            if len(tmp) == 1:
                print(Cx, Cy, *list(tmp))
                exit()


if __name__ == '__main__':
    resolve()
