# https://atcoder.jp/contests/sumitrust2019/submissions/14642156
# D - Lucky PIN
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input()
    num = list(set(s))
    res = 0
    for i in num:
        for j in num:
            for k in num:
                ss = i + j + k
                pos = 0
                for l in range(len(s)):
                    if ss[pos] == s[l]:
                        pos += 1
                        if pos == 3:
                            res += 1
                            break
    print(res)


if __name__ == '__main__':
    resolve()
