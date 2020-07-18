# https://atcoder.jp/contests/joi2008ho/submissions/15306510
# A - 碁石ならべ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    res = 0
    cnt_w = cnt_b = 0
    cnt = []
    for i in range(n):
        c = int(input())
        if (i + 1) % 2 == 1:
            if c == 0:
                cnt_w += 1
                if cnt_b:
                    cnt.append(cnt_b)
                cnt_b = 0
            else:
                cnt_b += 1
                if cnt_w:
                    cnt.append(cnt_w)
                    res += cnt_w
                cnt_w = 0
        else:
            if c == 0:
                if cnt_b == 0:
                    cnt_w += 1
                else:
                    if len(cnt) != 0:
                        cnt_w = cnt_b + 1 + cnt[-1]
                        res -= cnt[-1]
                        cnt.pop()
                    else:
                        cnt_w = cnt_b + 1
                    cnt_b = 0
            else:
                if cnt_w == 0:
                    cnt_b += 1
                else:
                    if len(cnt) != 0:
                        cnt_b += cnt_w + 1 + cnt[-1]
                        cnt.pop()
                    else:
                        cnt_b += cnt_w + 1
                    cnt_w = 0
    if cnt_w:
        res += cnt_w
    print(res)


if __name__ == '__main__':
    resolve()
