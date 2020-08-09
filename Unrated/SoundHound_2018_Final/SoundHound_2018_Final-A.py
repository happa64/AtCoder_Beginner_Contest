# https://atcoder.jp/contests/soundhound2018-summer-final-open/submissions/15791520
# A - Feel the Beat
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def calc(x):
        min_bpm = 140
        max_bpm = 170
        res = 0
        while True:
            if max_bpm <= x:
                res += max_bpm - min_bpm
                min_bpm *= 2
                max_bpm *= 2
            elif min_bpm <= x < max_bpm:
                res += x - min_bpm + 1
                break
            else:
                break
        return res

    c, d = map(int, input().split())
    res = calc(d - 1) - calc(c - 1)
    print(res)


if __name__ == '__main__':
    resolve()
