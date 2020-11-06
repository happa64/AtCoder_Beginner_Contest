# https://atcoder.jp/contests/nikkei2019-2-final/submissions/17908374
# B - NIKKEI String
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    n = len(S)
    res = 0
    for i in range(2, n - 2):
        for j in range(i + 2, n - 1, 2):
            a = S[:i]
            b = S[i:j]
            c = S[j:]
            if b[:len(b) // 2] != b[len(b) // 2:]:
                continue
            l = min(len(a), len(c))
            k = 1
            while k < l:
                if a[-k] == c[-k]:
                    res += 1
                    k += 1
                else:
                    break
    print(res)


if __name__ == '__main__':
    resolve()
