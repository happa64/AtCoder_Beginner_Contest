# https://atcoder.jp/contests/code-festival-2014-final/submissions/14799687
# B - 暗算ゲーム
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    res = 0
    for i in range(len(s)):
        if i % 2 == 0:
            res += int(s[i])
        else:
            res -= int(s[i])
    print(res)


if __name__ == '__main__':
    resolve()
