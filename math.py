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

    def divide_integers_bitwise(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        '''
        Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

        Return the quotient after dividing dividend by divisor.
        
        The integer division should truncate toward zero.
        
        Example 1:
        
        Input: dividend = 10, divisor = 3
        Output: 3
        Example 2:
        
        Input: dividend = 7, divisor = -3
        Output: -2
        Note:
        
        Both dividend and divisor will be 32-bit signed integers.
        The divisor will never be 0.
        Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.'''

        negative = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            negative = True
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        while dividend >= divisor:
            quotient = 1
            div = divisor
            while div << 1 <= dividend:
                div <<= 1
                quotient <<= 1
            dividend -= div
            result += quotient

        if negative:
            return -result
        else:
            return result




def main():
    m = Math()
    m.title_to_number("ZY")


if __name__ == "__main__":
    main()