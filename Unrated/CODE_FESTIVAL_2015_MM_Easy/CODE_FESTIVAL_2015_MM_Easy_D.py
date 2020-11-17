# https://atcoder.jp/contests/code-festival-2015-morning-easy/submissions/18188846
# B - ヘイホー君と置き換え
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    if n % 2:
        print(-1)
        exit()

    S = input().rstrip()
    s = S[:n // 2]
    t = S[n // 2:]
    res = 0
    for i in range(n // 2):
        if s[i] != t[i]:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
