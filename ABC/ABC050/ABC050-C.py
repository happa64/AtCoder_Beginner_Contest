# https://atcoder.jp/contests/arc066/tasks/arc066_a
# C - Lining Up
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = sorted(list(map(int, input().split())))

    # 報告に矛盾が無い場合、答えは2 ** (n // 2) である
    # 人数が偶数である場合、報告は・・・10,8,6,4,2,0,2,4,6,8,10・・・とならない限り矛盾する
    if n % 2 != 0:
        for i in range(n):
            if i == 0:
                if A[i] != 0:
                    print(0)
                    break
            else:
                if i % 2 != 0:
                    if A[i] - A[i - 1] != 2:
                        print(0)
                        break
                else:
                    if A[i] != A[i - 1]:
                        print(0)
                        break
        else:
            res = pow(2, n // 2, mod)
            print(res)

    # 人数が奇数である場合、報告は・・・11,9,7,5,3,1,1,3,5,7,9,11・・・とならない限り矛盾する
    else:
        for i in range(n):
            if i == 0:
                if A[i] != 1:
                    print(0)
                    break
            else:
                if i % 2 == 0:
                    if A[i] - A[i - 1] != 2:
                        print(0)
                        break
                else:
                    if A[i] != A[i - 1]:
                        print(0)
                        break
        else:
            res = pow(2, n // 2, mod)
            print(res)


if __name__ == '__main__':
    resolve()
