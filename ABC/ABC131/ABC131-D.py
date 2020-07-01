# https://atcoder.jp/contests/abc131/submissions/12926872
# D - Megalomania
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    # 締切が早い順に仕事を消化していく
    AB = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])

    total = 0
    for a, b in AB:
        total += a
        if total > b:
            print("No")
            break
    else:
        print("Yes")


if __name__ == '__main__':
    resolve()
