# https://atcoder.jp/contests/arc003/submissions/14445990
# A - GPA計算
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    r = input()
    score = r.count("A") * 4 + r.count("B") * 3 + r.count("C") * 2 + r.count("D")
    print(score / n)


if __name__ == '__main__':
    resolve()
