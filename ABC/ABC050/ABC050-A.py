# https://atcoder.jp/contests/abc050/submissions/14206508
# A - Addition and Subtraction Easy
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    fomula = input()
    print(eval(fomula))


if __name__ == '__main__':
    resolve()
