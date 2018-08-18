'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class ClosestSum:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        sum = nums[0] + nums[1] + nums[len(nums) - 1]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(curr_sum - target) < abs(sum - target):
                    sum = curr_sum
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1



        return sum

def main():
    s = ClosestSum()
    nums = [-1, 2, 1, -4]
    target = 2
    print(s.threeSumClosest(nums, target))
    #print(permutation.permuteRec("abc"))
if __name__ == "__main__":
    main()

