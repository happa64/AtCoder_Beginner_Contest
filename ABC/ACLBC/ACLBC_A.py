# https://atcoder.jp/contests/abl/submissions/17020679
# A - Repeat ACL
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    k = int(input())
    res = ""
    for _ in range(k):
        res += "ACL"
    print(res)

if __name__ == '__main__':
    resolve()
