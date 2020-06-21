# https://atcoder.jp/contests/arc019/submissions/14512183
# A - お買い物クライシス
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    res = s.replace("O","0").replace("D","0").replace("I","1").replace("Z","2").replace("S","5").replace("B","8")
    print(res)


if __name__ == '__main__':
    resolve()
