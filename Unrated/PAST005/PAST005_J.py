# https://atcoder.jp/contests/past202012-open/submissions/19096398
# J - 長い長い文字列
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    x = int(input())

    last = S[0]
    while True:
        length = 0
        for s in S:
            if not s.isdigit():
                if length + 1 == x:
                    print(s)
                    return
                length += 1
                last = s
            else:
                if length * (int(s) + 1) > x:
                    x -= length
                    break
                elif length * (int(s) + 1) == x:
                    print(last)
                    return
                length += length * int(s)


if __name__ == '__main__':
    resolve()
