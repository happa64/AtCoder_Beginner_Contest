# https://atcoder.jp/contests/past201912-open/tasks/past201912_f
# F - DoubleCamelCase Sort
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = str(input())

    res = []
    i = 1
    k = 0
    # 文字列を前から見ていき、大文字があったら、先頭からそこまでを配列に追加
    # 先頭を更新し、これを繰り返す
    while i <= len(s):
        if s[i].isupper():
            res.append(s[k: i + 1])
            k = i + 1
            i += 1
        i += 1

    res = sorted(res, key=str.lower)
    print("".join(res))

    # 以下のコードの方がスマート
    # import re
    #
    # s = re.findall(r'[A-Z][a-z]*[A-Z]', input())
    # s.sort(key=lambda s: s.lower())
    # print(''.join(s))


if __name__ == '__main__':
    resolve()
