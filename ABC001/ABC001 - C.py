# https://atcoder.jp/contests/abc001/tasks/abc001_3
# C - 風力観測
import sys

sys.setrecursionlimit(10 ** 7)


def resolve():
    Dir, w = map(int, input().split())

    if 112.5 <= Dir < 337.5:
        Dir = "NNE"
    elif 337.5 <= Dir < 562.5:
        Dir = "NE"
    elif 562.5 <= Dir < 787.5:
        Dir = "ENE"
    elif 787.5 <= Dir < 1012.5:
        Dir = "E"
    elif 1012.5 <= Dir < 1237.5:
        Dir = "ESE"
    elif 1237.5 <= Dir < 1462.5:
        Dir = "SE"
    elif 1462.5 <= Dir < 1687.5:
        Dir = "SSE"
    elif 1687.5 <= Dir < 1912.5:
        Dir = "S"
    elif 1912.5 <= Dir < 2137.5:
        Dir = "SSW"
    elif 2137.5 <= Dir < 2362.5:
        Dir = "SW"
    elif 2362.5 <= Dir < 2587.5:
        Dir = "WSW"
    elif 2587.5 <= Dir < 2812.5:
        Dir = "W"
    elif 2812.5 <= Dir < 3037.5:
        Dir = "WNW"
    elif 3037.5 <= Dir < 3262.5:
        Dir = "NW"
    elif 3262.5 <= Dir < 3487.5:
        Dir = "NNW"
    else:
        Dir = "N"

    if w < 0.25 * 60:
        W = 0
        Dir = "C"
    elif 0.25 * 60 <= w < 1.55 * 60:
        W = 1
    elif 1.55 * 60 <= w < 3.35 * 60:
        W = 2
    elif 3.35 * 60 <= w < 5.45 * 60:
        W = 3
    elif 5.45 * 60 <= w < 7.95 * 60:
        W = 4
    elif 7.95 * 60 <= w < 10.75 * 60:
        W = 5
    elif 10.75 * 60 <= w < 13.85 * 60:
        W = 6
    elif 13.85 * 60 <= w < 17.15 * 60:
        W = 7
    elif 17.15 * 60 <= w < 20.75 * 60:
        W = 8
    elif 20.75 * 60 <= w < 24.45 * 60:
        W = 9
    elif 24.45 * 60 <= w < 28.45 * 60:
        W = 10
    elif 28.45 * 60 <= w < 32.65 * 60:
        W = 11
    elif 32.65 * 60 <= w:
        W = 12

    print(Dir, W)


if __name__ == '__main__':
    resolve()
