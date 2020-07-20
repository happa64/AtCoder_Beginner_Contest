# https://atcoder.jp/contests/digitalarts2012/submissions/15336329
# B - Password
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    C = input()
    if C == "zzzzzzzzzzzzzzzzzzzz" or C == "a":
        print("NO")
    elif C != C[::-1]:
        print(C[::-1])
    else:
        hash = sum([ord(c) - 96 for c in C])
        num = 26
        while True:
            res = ""
            t = hash
            while t >= num:
                res += chr(96 + num)
                t -= num
            if t:
                res += chr(96 + t)
            if res == C:
                num -= 1
            else:
                print(res)
                break


if __name__ == '__main__':
    resolve()
