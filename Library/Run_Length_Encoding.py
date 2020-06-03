class RunLengthEncoding:
    def __init__(self, s):
        self.s = s
        self.ans = ""
        self.count = 0

    def encoding(self):
        tmp = self.s[0]
        for i in range(len(s)):
            if tmp == s[i]:
                self.count += 1
            else:
                self.ans += tmp + str(self.count)
                self.count = 1
                tmp = s[i]
        return self.ans + tmp + str(self.count)

