class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss, last_max, max_len = '', 0, 0
        for each in s:
            if each in ss:
                ss = ss.split(each)[-1] + each
                last_max = len(ss)

            else:
                ss += each
                last_max += 1
                if last_max > max_len:
                    max_len = last_max
        print(ss)
        return max_len


def main():
    s = Solution()
    print(s.lengthOfLongestSubstring("hkcpmprxxxqw"))

if __name__ == "__main__":
    main()


