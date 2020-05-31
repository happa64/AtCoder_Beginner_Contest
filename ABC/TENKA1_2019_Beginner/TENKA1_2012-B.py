# https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_b
# B - *e**** ********e* *e****e* ****e**
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = list(input())
    k = int(input())

    for i in range(n):
        if s[i] != s[k - 1]:
            s[i] = "*"

    print("".join(s))


if __name__ == '__main__':
    resolve()
