# https://atcoder.jp/contests/hhkb2020/submissions/17287601
# A - Keyboard
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    T = input()
    print(T.upper() if S == "Y" else T)


if __name__ == '__main__':
    resolve()
