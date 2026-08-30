class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # brute force
        zero_count = 0
        one_count = 0
        two_count = 0

        for n in nums:
            if n == 0:
                zero_count += 1
            elif n == 1:
                one_count += 1
            else:
                two_count += 1
        
        idx = 0
        while (zero_count > 0):
            nums[idx] = 0
            idx += 1
            zero_count -= 1

        while one_count > 0:
            nums[idx] = 1
            idx += 1
            one_count -= 1

        while two_count > 0:
            nums[idx] = 2
            idx += 1
            two_count -= 1


        # Optimized Approach
        # low = 0
        # mid = 0
        # high = len(nums) - 1
        
        # # One-pass scan
        # while mid <= high:
        #     if nums[mid] == 0:
        #         # Swap mid with low, move both forward
        #         nums[low], nums[mid] = nums[mid], nums[low]
        #         low += 1
        #         mid += 1
        #     elif nums[mid] == 1:
        #         # It's in the correct middle region, just move mid forward
        #         mid += 1
        #     else: # nums[mid] == 2
        #         # Swap mid with high, push 2 to the end. 
        #         # Don't increment mid yet because the swapped element needs checking!
        #         nums[mid], nums[high] = nums[high], nums[mid]
        #         high -= 1


        