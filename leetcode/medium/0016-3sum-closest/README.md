# 3Sum Closest

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer array `nums` of length `n` and an integer `target`.

Find three integers at  **distinct indices**  in `nums` such that the sum is  **closest**  to `target`.

Return the sum of the three integers.

You may assume that each input would have  **exactly**  one solution.

 

 **Example 1:** 

```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

```

 **Example 2:** 

```
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

```

 

 **Constraints:** 

- 3 <= nums.length <= 500
- -1000 <= nums[i] <= 1000
- -104 <= target <= 104

## Solution

**Language:** Python  
**Runtime:** 353 ms (beats 81.12%)  
**Memory:** 19 MB (beats 99.00%)  
**Submitted:** 2026-10-30T06:59:56.080Z  

```py
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        result = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]

                if abs(current - target) < abs(result - target):
                    result = current

                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    return current

        return result
```

---

[View on LeetCode](https://leetcode.com/problems/3sum-closest/)