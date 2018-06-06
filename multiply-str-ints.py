'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

def multiply(num1, num2):
    """
            :type num1: str
            :type num2: str
            :rtype: str
            """

    dict_int = {str(i): i for i in range(10)}

    def str_to_int(num):
        num_int = 0
        for idx, char in enumerate(num):
            num_int += dict_int[char] * (10**(len(num) - idx - 1))
        return num_int

    return str(str_to_int(num1) * str_to_int(num2))

print(multiply("23", "20"))