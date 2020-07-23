# https://atcoder.jp/contests/tenka1-2012-qualB/submissions/15379937
# B - camel_case
import sys
import re

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    lu, s, tu = re.fullmatch(r'(_*)(.*?)(_*)', input()).groups()

    if re.fullmatch(r'[a-z][0-9a-z]*(?:_[a-z][0-9a-z]*)*', s):
        ss = s.split('_')
        s = ss[0] + ''.join(list(map(str.capitalize, ss[1:])))
    elif re.fullmatch(r'[a-z][0-9a-z]*(?:[A-Z][0-9a-z]*)*', s):
        s = '_'.join(re.split(r'(?=[A-Z])', s)).lower()

    print(lu + s + tu)


if __name__ == '__main__':
    resolve()
