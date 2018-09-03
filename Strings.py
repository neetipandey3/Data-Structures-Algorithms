class Strings:
    def reverse(self, x):
        """
        :type x: string
        :rtype: string
        """
        return x[::-1]

    def reverse_int(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            rev = int("-"+str(abs(x))[::-1])
        else:
            rev = int(str(x)[::-1])
        if rev < -2**31 or rev > 2**31 - 1:
            rev = 0
        return rev

    def is_anagram(self, s, t):

        """
        :type s: str
        :type t: str
        :rtype: bool

        Given two strings s and t , write a function to determine if t is an anagram of s.

        Example 1:

        Input: s = "anagram", t = "nagaram"
        Output: true
        Example 2:

        Input: s = "rat", t = "car"
        Output: false
        Note:
        You may assume the string contains only lowercase alphabets.
        """
        return sorted(s) == sorted(t)

    def is_palindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #s = list(filter(lambda c: c.isalpha() or c.isdigit(), s))
        s = list(filter(lambda c: c.isalnum(), s))
        s = ("".join(s)).lower()
        #print(s)

        if len(s) in (0, 1):
            return True
        for i in range(len(s)):
            if s[i] != s[-(i+1)]:
                return False

        return True

    def first_uniq_char(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        counter = [0] * 26
        for x in s:
            counter[ord(x) - ord('a')] += 1

        for idx, x in enumerate(s):
            if counter[ord(x) - ord('a')] == 1:
                return idx

        return -1



def main():
    s = Strings()

    print(s.reverse_int(-123))
    print(s.is_anagram("anagram", "nagaram"))
    print(s.is_palindrome("A man, a plan, a canal: Panama"))
    print(s.first_uniq_char("falafals"))
if __name__ == "__main__":
    main()

