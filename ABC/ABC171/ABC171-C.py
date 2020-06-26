# https://atcoder.jp/contests/abc171/submissions/14689250
# C - One Quadrillion and One Dalmatians
import sys

sys.setrecursionlimit(10 ** 7)

f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    L = [chr(i) for i in range(97, 97 + 26)]

    res = ""
    while n:
        r = n % 26
        res += L[r - 1]
        n = max(0, (n - 1)) // 26
    print(res[::-1])


if __name__ == '__main__':
    resolve()
