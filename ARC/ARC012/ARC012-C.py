# https://atcoder.jp/contests/arc012/submissions/18542047
# C - 五目並べチェッカー
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def f(tmp, L):
        if len(tmp) >= 10:
            print("NO")
            exit()
        if len(tmp) >= 5:
            for _ in range(len(tmp) - 5):
                tmp.pop(0)
                tmp.pop()
            L.append(set(tmp))
        return L

    def calc(color):
        L = []
        for h in range(19):
            tmp = []
            for w in range(19):
                if grid[h][w] == color:
                    tmp.append(h * 19 + w)
                else:
                    L = f(tmp, L)
                    tmp = []
            L = f(tmp, L)

        for w in range(19):
            tmp = []
            for h in range(19):
                if grid[h][w] == color:
                    tmp.append(h * 19 + w)
                else:
                    L = f(tmp, L)
                    tmp = []
            L = f(tmp, L)

        for s in range(2 * 18 + 1):
            a = max(0, s - 18)
            b = min(18, s)
            w = s - a
            tmp = []
            for h in range(a, b + 1):
                if grid[h][w] == color:
                    tmp.append(h * 19 + w)
                else:
                    L = f(tmp, L)
                    tmp = []
                w -= 1
            L = f(tmp, L)

        for s in range(-18, 19):
            a = max(0, -s)
            b = min(18, 18 - s)
            w = s + a
            tmp = []
            for h in range(a, b + 1):
                if grid[h][w] == color:
                    tmp.append(h * 19 + w)
                else:
                    L = f(tmp, L)
                    tmp = []
                w += 1
            L = f(tmp, L)
        return L

    grid = [input().rstrip() for _ in range(19)]

    cnt_black = cnt_white = 0
    for i in range(19):
        for j in range(19):
            if grid[i][j] == "o":
                cnt_black += 1
            elif grid[i][j] == "x":
                cnt_white += 1

    if not (cnt_black - cnt_white == 0 or cnt_black - cnt_white == 1):
        print("NO")
        exit()

    black = calc("o")
    while len(black) > 1:
        a = black.pop(0)
        b = black[0]
        if a & b:
            black[0] = a & b
        else:
            print("NO")
            exit()
    white = calc("x")
    while len(white) > 1:
        a = white.pop(0)
        b = white[0]
        if a & b:
            white[0] = a & b
        else:
            print("NO")
            exit()

    if not black and not white:
        print("YES")
    else:
        if cnt_white == cnt_black:
            if black:
                print("NO")
            else:
                print("YES")
        else:
            if white:
                print("NO")
            else:
                print("YES")


if __name__ == '__main__':
    resolve()
