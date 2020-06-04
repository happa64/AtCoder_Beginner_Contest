class RunLengthEncoding:
    def __init__(self, s):
        """
        :param s:エンコードもしくはデコードしたい文字列
        """
        self.s = s
        self.ans = ""
        self.count = 0

    def encoding(self):
        """
        :return:連長圧縮した文字列を返します
        """
        tmp = self.s[0]
        for i in range(len(s)):
            if tmp == s[i]:
                self.count += 1
            else:
                self.ans += tmp + str(self.count)
                self.count = 1
                tmp = s[i]
        return self.ans + tmp + str(self.count)

    def decoding(self):
        """
        :return:連長圧縮された文字列を元に戻した文字列を返します
        """
        tmp = self.s[0]
        num = ""
        i = 1
        while i < len(self.s):
            while i < len(self.s) and self.s[i].isdigit():
                num += self.s[i]
                i += 1
            self.ans += tmp * int(num)
            if i < len(self.s):
                tmp = self.s[i]
                num = ""
                i += 1
        return self.ans
