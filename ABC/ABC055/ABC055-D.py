# https://atcoder.jp/contests/abc055/submissions/13418609
# D - Menagerie
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要；
        隣接する2匹が決まれば、他の全ての配置が決定する為、最初の2匹を決め打ちし配置を決定した後、
        配置と証言に矛盾が生じないかチェックする。
        最初の2匹は[S, S][S, W][W, S][W, W]の4パターンである。

    計算量：O(4 * N)
    """

    n = int(input())
    s = input()
    L = ["S", "W"]

    # first:最初の1匹目、second：2匹目
    for first in L:
        for second in L:
            res = ["" for _ in range(n)]
            res[0] = first
            res[1] = second

            # 証言の通りに配置を決めていく
            for i in range(1, n - 1):
                if s[i] == "o":
                    if res[i] == "S" and res[i - 1] == "S":
                        res[i + 1] = "S"
                    elif res[i] == "S" and res[i - 1] == "W":
                        res[i + 1] = "W"
                    elif res[i] == "W" and res[i - 1] == "W":
                        res[i + 1] = "S"
                    else:
                        res[i + 1] = "W"
                else:
                    if res[i] == "S" and res[i - 1] == "S":
                        res[i + 1] = "W"
                    elif res[i] == "S" and res[i - 1] == "W":
                        res[i + 1] = "S"
                    elif res[i] == "W" and res[i - 1] == "W":
                        res[i + 1] = "W"
                    else:
                        res[i + 1] = "S"

            # 配置を決めた後、最後の一匹と最初の一匹の証言に矛盾が無いかチェックする。
            if s[-1] == "o":
                if (res[-1] == "S" and res[-2] != res[0]) or (res[-1] == "W" and res[-2] == res[0]):
                    continue
            else:
                if (res[-1] == "S" and res[-2] == res[0]) or (res[-1] == "W" and res[-2] != res[0]):
                    continue

            if s[0] == "o":
                if (res[0] == "S" and res[-1] != res[1]) or (res[0] == "W" and res[-1] == res[1]):
                    continue
            else:
                if (res[0] == "S" and res[-1] == res[1]) or (res[0] == "W" and res[-1] != res[1]):
                    continue

            # 矛盾がなければその配置が解となる
            print("".join(res))
            break
        else:
            continue
        break
    else:
        print(-1)


if __name__ == '__main__':
    resolve()
