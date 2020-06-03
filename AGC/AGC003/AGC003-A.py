# https://atcoder.jp/contests/agc003/tasks/agc003_a
# A - Wanna go back home
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()

    if ("S" in s and "N" not in s) or ("N" in s and "S" not in s):
        print("No")
    elif ("W" in s and "E" not in s) or ("E" in s and "W" not in s):
        print("No")
    else:
        print("Yes")



if __name__ == '__main__':
    resolve()
