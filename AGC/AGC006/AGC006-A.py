# https://atcoder.jp/contests/agc006/tasks/agc006_a
# A - Prefix and Suffix
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input()
    t = input()

    res = n
    for i in range(n):
        for j in range(n):
            if i + j < n:
                if s[i + j] != t[j]:
                    break
        else:
            res = i
            break

    print(res + n)


if __name__ == '__main__':
    resolve()
