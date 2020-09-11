# https://atcoder.jp/contests/agc022/submissions/16627444
# B - GCD Sequence
import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def debug(res):
    tot = sum(res)
    for num in res:
        if gcd(tot - num, num) == 1:
            return False
    return True


def resolve():
    n = int(input())

    if n == 3:
        res = [2, 5, 63]
    elif n == 4:
        res = [2, 5, 20, 63]
    elif n == 5:
        res = [2, 5, 20, 30, 63]
    else:
        nums = [num for num in range(2, 30001) if num % 2 == 0 or num % 3 == 0]
        res = [nums[i] for i in range(n)]
        total = sum(res)
        if total % 6 == 2:
            res.pop(res.index(8))
            for i in range(n, len(nums)):
                if nums[i] % 6 == 0:
                    res.append(nums[i])
                    break
        elif total % 6 == 3:
            res.pop(res.index(9))
            for i in range(n, len(nums)):
                if nums[i] % 6 == 0:
                    res.append(nums[i])
                    break
        elif total % 6 == 5:
            res.pop(res.index(9))
            for i in range(n, len(nums)):
                if nums[i] % 6 == 4:
                    res.append(nums[i])
                    break
    print(*res)
    # print(debug(res))


if __name__ == '__main__':
    resolve()
