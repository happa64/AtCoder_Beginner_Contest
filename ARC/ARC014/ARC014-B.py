# https://atcoder.jp/contests/arc014/submissions/14422894
# B - あの日したしりとりの結果を僕達はまだ知らない。
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    T1, T2 = [], []
    for i in range(n):
        w = input()
        if i % 2 == 0:
            T1.append(w)
        else:
            T2.append(w)

    used = set()
    flg = 1
    prev = T1.pop(0)
    used.add(prev)
    while T1 or T2:
        if not flg:
            word = T1.pop(0)
            if word in used or word[0] != prev[-1]:
                print("LOSE")
                break
            flg ^= 1
            prev = word
            used.add(prev)
        else:
            word = T2.pop(0)
            if word in used or word[0] != prev[-1]:
                print("WIN")
                break
            flg ^= 1
            prev = word
            used.add(prev)
    else:
        print("DRAW")


if __name__ == '__main__':
    resolve()
