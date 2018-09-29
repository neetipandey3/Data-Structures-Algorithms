class Math:
    def title_to_number(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''
        Given a column title as appear in an Excel sheet, return its corresponding column number.

        For example:
        
            A -> 1
            B -> 2
            C -> 3
            ...
            Z -> 26
            AA -> 27
            AB -> 28 
            ...
        Example 1:
        
        Input: "A"
        Output: 1
        Example 2:
        
        Input: "AB"
        Output: 28
        Example 3:
        
        Input: "ZY"
        Output: 701
        '''
        label = s[::-1]
        result = 0
        for i, c in enumerate(label):
            if i == 0:
                result += (ord(c) - ord('A') + 1)
                continue
            result += (26 ** (i)) * (ord(c) - ord('A') + 1)
        return result

def main():
    m = Math()
    m.title_to_number("ZY")


if __name__ == "__main__":
    main()