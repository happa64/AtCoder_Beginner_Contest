# https://atcoder.jp/contests/abc001/tasks/abc001_2
# B - 視程の通報
import sys

sys.setrecursionlimit(10 ** 7)


def resolve():
    m = int(input())
    if m < 100:
        print("00")
    elif 100 <= m <= 5000:
        res = int((m / 1000) * 10)
        if len(str(res)) == 1:
            print("0" + str(res))
        else:
            print(res)
    elif 6000 <= m <= 30000:
        print((m // 1000) + 50)
    elif 35000 <= m <= 70000:
        print(((m // 1000) - 30) // 5 + 80)
    else:
        print(89)


if __name__ == '__main__':
    resolve()
