# https://atcoder.jp/contests/code-festival-2017-qualc/tasks/code_festival_2017_qualc_c
# C - Inserting 'x'
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    ss = []
    for i in s:
        if i != "x":
            ss.append(i)

    # xを除いた文字列が回文でなければ-1を出力
    if ss != ss[::-1]:
        print(-1)
    else:
        n = len(ss) + 1
        cnt = 0
        cnt_x = [0] * n
        pos = 0
        # x以外の文字の間に存在しているxをカウント
        for i in range(len(s)):
            if s[i] == "x":
                cnt += 1

            if s[i] != "x" or i == len(s) - 1:
                cnt_x[pos] = cnt
                cnt = 0
                pos += 1

        # カウントしたxの配列を先頭と末尾から舐めていき、差の絶対値の和が答えとなる
        res = 0
        for i in range(n // 2):
            res += abs(cnt_x[i] - cnt_x[-(i + 1)])

        print(res)


if __name__ == '__main__':
    resolve()
