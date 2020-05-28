# https://atcoder.jp/contests/past202004-open/tasks/past202004_a
# A - エレベーター
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s, t = map(str, input().split())

    if s[1] == "F" and t[1] == "F":
        print(abs(int(t[0]) - int(s[0])))
    elif s[0] == "B" and t[0] == "B":
        print(abs(int(t[1]) - int(s[1])))
    elif s[1] == "F" and t[0] == "B":
        print(int(s[0]) + int(t[1]) - 1)
    elif s[0] == "B" and t[1] == "F":
        print(int(t[0]) + int(s[1]) - 1)


if __name__ == '__main__':
    resolve()
