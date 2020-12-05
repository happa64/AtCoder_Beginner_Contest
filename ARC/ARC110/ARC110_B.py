# https://atcoder.jp/contests/arc110/submissions/18586153
# B - Many 110
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    T = input()

    i = 0
    cnt = 0
    flg = False
    head = ""
    while i < n - 2:
        t = T[i:i + 3]
        if t != "110":
            if not flg:
                head += T[i]
                i += 1
            else:
                print(0)
                exit()
        else:
            flg = True
            cnt += 1
            i += 3

    foot = T[len(head) + cnt * 3:]
    if cnt == 0:
        if n > 5:
            print(0)
            exit()
        elif n == 4:
            if T == "1011":
                print(9999999999)
            else:
                print(0)
        elif n == 3:
            if T == "110":
                print(pow(10, 10))
            elif T == "101":
                print(9999999999)
            elif T == "011":
                print(9999999999)
            else:
                print(0)
        elif n == 2:
            if T == "11":
                print(pow(10, 10))
            elif T == "10":
                print(pow(10, 10))
            elif T == "01":
                print(9999999999)
            else:
                print(0)
        else:
            if T == "1":
                print(pow(10, 10) * 2)
            else:
                print(pow(10, 10))
        exit()
    else:
        if not (head == "" or head == "0" or head == "10") and (
                foot == "" or foot == "1" or foot == "11"):
            print(0)
            exit()

    if head != "":
        cnt += 1

    if foot != "":
        cnt += 1

    res = pow(10, 10) - cnt
    print(res + 1)


if __name__ == '__main__':
    resolve()
