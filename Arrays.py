class Array:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = len(nums)-1
        while i > 0:
            if nums[i] == nums[i-1]:
                del(nums[i])
            else:
                i -= 1
        return len(nums)

    def removeDuplicatesSet(self, nums):
        nums[:] = set(nums)
        nums.sort()
        return len(nums)

    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #n = len(nums)
        #nums[:] = nums[n - k:] + nums[:n - k]

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums[:] = [nums.pop()] + nums

    def contains_duplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
        #import numpy as np
        #nums = np.array(nums)
        #return True if np.unique(nums).size < nums.size else False

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]


        Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

        The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

        You may assume the integer does not contain any leading zero, except the number 0 itself.

        Example 1:

        Input: [1,2,3]
        Output: [1,2,4]
        Explanation: The array represents the integer 123.
        Example 2:

        Input: [4,3,2,1]
        Output: [4,3,2,2]
        Explanation: The array represents the integer 4321.
        """

        for i in range(len(digits)):
            if digits[len(digits) - 1 - i] + 1 > 9:
                if len(digits) - 1 - i == 0:
                    return [1] + [0] + digits[1:]
                digits[len(digits) - 1 - i] = 0
                self.plusOne(digits[:len(digits) - i])
            else:
                digits[len(digits) - 1 - i] += 1
                return digits

        def moveZeroes(self, nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.


            Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

            Example:

            Input: [0,1,0,3,12]
            Output: [1,3,12,0,0]
            Note:

            You must do this in-place without making a copy of the array.
            Minimize the total number of operations.

            """
            for _ in range(nums.count(0)):
                nums.remove(0)
                nums.append(0)

        def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]

            Given an array of integers, return indices of the two numbers such that they add up to a specific target.

            You may assume that each input would have exactly one solution, and you may not use the same element twice.

            Example:

            Given nums = [2, 7, 11, 15], target = 9,

            Because nums[0] + nums[1] = 2 + 7 = 9,
            return [0, 1].

            """
            for i in range(len(nums)):
                rem = target - nums[i]
                for j in range(i + 1, len(nums)):
                    if i != j:
                        if nums[j] == rem:
                            return [i, j]

        def rotate(self, matrix):
            """
            :type matrix: List[List[int]]
            :rtype: void Do not return anything, modify matrix in-place instead.
            You are given an n x n 2D matrix representing an image.

            Rotate the image by 90 degrees (clockwise).

            Note:

            You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

            Example 1:

            Given input matrix =
            [
              [1,2,3],
              [4,5,6],
              [7,8,9]
            ],

            rotate the input matrix in-place such that it becomes:
            [
              [7,4,1],
              [8,5,2],
              [9,6,3]
            ]
            Example 2:

            Given input matrix =
            [
              [ 5, 1, 9,11],
              [ 2, 4, 8,10],
              [13, 3, 6, 7],
              [15,14,12,16]
            ],

            rotate the input matrix in-place such that it becomes:
            [
              [15,13, 2, 5],
              [14, 3, 4, 1],
              [12, 6, 8, 9],
              [16, 7,10,11]
            ]
            """
            matrix[::] = zip(*matrix[::-1])

    def three_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]


        Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

        Note:

        The solution set must not contain duplicate triplets.

        Example:

        Given array nums = [-1, 0, 1, 2, -1, -4],

        A solution set is:
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]



        """
        nums.sort()
        result = []
        n = len(nums)
        if not nums or len(nums) < 3:
            return []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1

        return result

    def set_zeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

        Example 1:

        Input:
        [
          [1,1,1],
          [1,0,1],
          [1,1,1]
        ]
        Output:
        [
          [1,0,1],
          [0,0,0],
          [1,0,1]
        ]
        Example 2:

        Input:
        [
          [0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]
        ]
        Output:
        [
          [0,0,0,0],
          [0,4,5,0],
          [0,3,1,0]
        ]
        Follow up:

        A straight forward solution using O(mn) space is probably a bad idea.
        A simple improvement uses O(m + n) space, but still not the best solution.
        Could you devise a constant space solution?



        """



        #Constnat space solution
        if not matrix:
            return []

        is_row_zero = False
        is_col_zero = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                is_col_zero = True
                break
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                is_row_zero = True
                break
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for i in range(1, len(matrix[0])):
                    matrix[row][i] = 0
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][col] = 0

        if is_row_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if is_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0


def main():
    a = Array()
    #nums = [0,0,1,1,1,2,2,3,3,4]
    nums = [1,1,2]
    #print(a.removeDuplicates(nums))

    #print(a.removeDuplicatesSet(nums))

    nums = [1, 2, 3, 4, 5, 6, 7]
    print(a.rotate2(nums, 3))
    print(a.three_sum([-1, 0, -1, 1, 2]))
    print(a.set_zeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]))

if __name__ == "__main__":
    main()


