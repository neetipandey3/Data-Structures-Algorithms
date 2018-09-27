class SortAndSearch:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.

        Example:

        Input:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3

        Output: [1,2,2,3,5,6]
        """
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if m == 0 and n > 0:
            nums1[:n] = nums2[:n]

    def top_k_frequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        '''Given a non-empty array of integers, return the k most frequent elements.
        
        Example 1:
        
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
        Example 2:
        
        Input: nums = [1], k = 1
        Output: [1]
        Note:
        
        You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
        Your algorithm's time complexity must be better than O(n log n), where n is the array's size.'''

        from collections import defaultdict
        d, freq = defaultdict(int), defaultdict(list)
        for n in nums:
            d[n] += 1
        for num, v in d.items():
            freq[v].append(num)

        result = []
        for frq in range(len(nums), -1, -1):
            if frq in freq:
                result += freq[frq]
            if len(result) == k:
                break

        return result

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        '''for i in range(k):
            if i == k-1:
                return max(nums)
            nums.remove(max(nums))'''

        return heapq.nlargest(k, nums)[-1]


def main():
    s = SortAndSearch()
    print(s.top_k_frequent([1, 1, 1, 2, 3, 4, 4, 4, 4 , 2]))




if __name__ == "__main__":
    main()

