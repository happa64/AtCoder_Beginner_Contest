# https://atcoder.jp/contests/colopl2018-qual/submissions/15472698
# B - すぬけそだて――チュートリアル――
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, x = map(int, input().split())
    s = input()
    res = 0
    for i in range(n):
        t = int(input())
        if s[i] == "0":
            res += t
        else:
            res += x if t > x else t
    print(res)


if __name__ == '__main__':
    resolve()
