# https://atcoder.jp/contests/abc019/submissions/13450626
# B - 高橋くんと文字列圧縮
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()

    # ランレングス圧縮
    def rle(s):
        tmp, count, ans = s[0], 1, ""
        for i in range(1, len(s)):
            if tmp == s[i]:
                count += 1
            else:
                ans += tmp + str(count)
                tmp = s[i]
                count = 1
        ans += tmp + str(count)
        return ans

    print(rle(s))


if __name__ == '__main__':
    resolve()
