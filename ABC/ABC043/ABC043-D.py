# https://atcoder.jp/contests/arc059/submissions/13456304
# D - アンバランス
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要：
        実は、アンバランスな部分文字列になる条件は以下の二つである。
        ①：1種類の文字が連続している EX) aa
        ②：1種類の文字が一種類の文字を挟んでいる EX) aba
        なので、この二つが文字列に含まれているか調べるだけでよい

    計算量：O(N)
    :return:
    """
    s = input()
    n = len(s)

    for i in range(1, n):
        if s[i - 1] == s[i]:
            print(i, i + 1)
            exit()

    for j in range(2, n):
        if s[j - 2] == s[j]:
            print(j - 1, j + 1)
            exit()

    print(-1, -1)


if __name__ == '__main__':
    resolve()
