# https://atcoder.jp/contests/abc171/submissions/14687839
# A - αlphabet
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    if s.isupper():
        print("A")
    else:
        print("a")



if __name__ == '__main__':
    resolve()
