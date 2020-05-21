# https://atcoder.jp/contests/abc039/submissions/13451377
# C - ピアニスト高橋君
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    temp = ["Fa", "Mi", "Re", "Re", "Do", "Do", "Si", "La", "La", "So", "So", "Fa"]
    print(temp[s.find("WBWBWBW")])


if __name__ == '__main__':
    resolve()
