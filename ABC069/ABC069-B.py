# https://atcoder.jp/contests/abc069/tasks/abc069_b
# B - i18n
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    res = ""
    cnt = 0
    for i in range(len(s)):
        if i == 0:
            res += s[i]
        elif i == len(s) - 1:
            res += str(cnt) + s[i]
        else:
            cnt += 1

    print(res)


if __name__ == '__main__':
    resolve()
