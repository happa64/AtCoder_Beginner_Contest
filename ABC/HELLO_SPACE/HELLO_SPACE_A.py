# https://atcoder.jp/contests/zone2021/submissions/22198898
# A - UFO襲来
import sys

sys.setrecursionlimit(10 ** 7)
if sys.platform == 'ios':
    sys.stdin = open('input_file.txt')
else:
    input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    S = input().rstrip()
    T = "ZONe"
    n = 12

    res = 0
    for i in range(n):
        s = S[i:i + 4]
        if s == T:
            res += 1
    print(res)


if __name__ == '__main__':
    solve()
