# https://atcoder.jp/contests/abc138/submissions/13631988
# E - Strings of Impurity
import sys
import bisect

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7
alphabet = [chr(i) for i in range(97, 97 + 26)]


def resolve():
    S = input()
    T = input()

    n = len(S)
    m = len(T)

    idx = [[] for _ in range(26)]
    for i in range(n):
        idx[alphabet.index(S[i])].append(i)

    for i in range(n):
        idx[alphabet.index(S[i])].append(i + n)

    res = 0
    pos = 0
    for i in range(m):
        c = alphabet.index(T[i])
        if len(idx[c]) == 0:
            print(-1)
            break
        pos = idx[c][bisect.bisect_left(idx[c], pos)] + 1
        if pos >= n:
            pos -= n
            res += n
    else:
        res += pos
        print(res)


if __name__ == '__main__':
    resolve()
