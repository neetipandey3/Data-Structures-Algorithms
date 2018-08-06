'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
'''

class Solution:
    def findRepeatedDnaSequences2(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = 10
        match = []
        for i in range(len(s)):
            if len(s[i:]) >= 10:
                ss = s[i:i+l]
            for j in range(i+1, len(s)):
                if len(s[j:]) >= 10:
                    ss2 = s[j: j+l]
                    if ss == ss2 and ss not in match:
                        match.append(ss)
        return match

    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = 10
        match = list()
        for i in range(len(s)):
            if len(s[i:]) >= 10:
                match.append(s[i:i+l])
        from collections import Counter
        match_c = Counter(match)

        return [x[0] for x in match_c.items() if x[1] > 1]


def main():
    s = Solution()
    print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

if __name__ == "__main__":
    main()