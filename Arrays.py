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
        import numpy as np
        nums = np.array(nums)
        return True if np.unique(nums).size < nums.size else False



def main():
    a = Array()
    #nums = [0,0,1,1,1,2,2,3,3,4]
    nums = [1,1,2]
    #print(a.removeDuplicates(nums))

    #print(a.removeDuplicatesSet(nums))

    nums = [1, 2, 3, 4, 5, 6, 7]
    print(a.rotate2(nums, 3))
if __name__ == "__main__":
    main()


