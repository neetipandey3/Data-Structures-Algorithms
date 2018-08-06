'''
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)
'''

class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        num = [int(i) for i in str(N)]

        idx = -1
        for i in range(len(num)-1, 0, -1):
            if num[i] < num[i-1]:
                num[i-1] -= 1
                idx = i
        if idx != -1:
            for i in range(idx, len(num)):
                num[i] = 9


        #if num[0] == 0:
            #num = num[1:]

        return int("".join(str(i) for i in num))

def main():
    s = Solution()
    print(s.monotoneIncreasingDigits("10"))

if __name__ == "__main__":
    main()