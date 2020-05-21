# https://atcoder.jp/contests/abc032/submissions/13452278
# B - 高橋君とパスワード
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    k = int(input())

    res = set()
    for i in range(len(s) - k + 1):
        res.add(s[i:i + k])

    print(len(res))


if __name__ == '__main__':
    resolve()
