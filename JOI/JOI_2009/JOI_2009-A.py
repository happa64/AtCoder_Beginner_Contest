# https://atcoder.jp/contests/joi2009ho/submissions/16281856
# A - IOIOI
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    m = int(input())
    s = input()

    cnt_list = []
    cnt = 0
    i = 1
    while i < m - 1:
        if s[i - 1] == "I" and s[i] == "O" and s[i + 1] == "I":
            cnt += 1
            i += 2
        else:
            if cnt:
                cnt_list.append(cnt)
            cnt = 0
            i += 1
    if cnt:
        cnt_list.append(cnt)

    res = 0
    for num in cnt_list:
        res += max(0, num - n + 1)
    print(res)


if __name__ == '__main__':
    resolve()
