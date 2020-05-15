# https://atcoder.jp/contests/abc071/submissions/12264449
# B - Not Found
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = set(input())
    for i in [chr(i) for i in range(97, 97 + 26)]:
        if i not in s:
            print(i)
            break
    else:
        print("None")


if __name__ == '__main__':
    resolve()
