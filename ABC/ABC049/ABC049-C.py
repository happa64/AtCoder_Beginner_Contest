# https://atcoder.jp/contests/abc049/submissions/13179780
# C - 白昼夢
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = list(input())
    S_Rev = S[::-1]
    n = len(S)

    pos = 0
    while pos < n:
        if S_Rev[pos] == "m":
            if pos + 5 <= n and "".join(S_Rev[pos:pos + 5]) == "maerd":
                pos += 5
            else:
                print("NO")
                break
        elif S_Rev[pos] == "e":
            if pos + 5 <= n and "".join(S_Rev[pos:pos + 5]) == "esare":
                pos += 5
            else:
                print("NO")
                break
        elif S_Rev[pos] == "r":
            if pos + 6 <= n and "".join(S_Rev[pos:pos + 6]) == "resare":
                pos += 6
            elif pos + 7 <= n and "".join(S_Rev[pos:pos + 7]) == "remaerd":
                pos += 7
            else:
                print("NO")
                break
        else:
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    resolve()
