# Sort Colors

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array `nums` with `n` objects colored red, white, or blue, sort them  **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

 **Example 1:** 

 **Input:**  nums = [2,0,2,1,1,0]

 **Output:**  [0,0,1,1,2,2]

 **Explanation:** 

The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.

 **Example 2:** 

 **Input:**  nums = [2,0,1]

 **Output:**  [0,1,2]

 **Explanation:** 

The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.

 

 **Constraints:** 

- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2.

 

 **Follow up:**  Could you come up with a one-pass algorithm using only constant extra space?

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.1 MB  
**Submitted:** 2026-08-30T06:20:05.031Z  

```py
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # brute force
        # zero_count = 0
        # one_count = 0
        # two_count = 0

        # for n in nums:
        #     if n == 0:
        #         zero_count += 1
        #     elif n == 1:
        #         one_count += 1
        #     else:
        #         two_count += 1
        
        # idx = 0
        # while (zero_count > 0):
        #     nums[idx] = 0
        #     idx += 1
        #     zero_count -= 1

        # while one_count > 0:
        #     nums[idx] = 1
        #     idx += 1
        #     one_count -= 1

        # while two_count > 0:
        #     nums[idx] = 2
        #     idx += 1
        #     two_count -= 1


        # Optimized Approach
        low = 0
        mid = 0
        high = len(nums) - 1
        
        # One-pass scan
        while mid <= high:
            if nums[mid] == 0:
                # Swap mid with low, move both forward
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # It's in the correct middle region, just move mid forward
                mid += 1
            else: # nums[mid] == 2
                # Swap mid with high, push 2 to the end. 
                # Don't increment mid yet because the swapped element needs checking!
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

---

[View on LeetCode](https://leetcode.com/problems/sort-colors/)