# Subarray Sum Equals K

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers `nums` and an integer `k`, return  *the total number of subarrays whose sum equals to*  `k`.

A subarray is a contiguous  **non-empty**  sequence of elements within an array.

 

 **Example 1:** 

```
Input: nums = [1,1,1], k = 2
Output: 2

```

 **Example 2:** 

```
Input: nums = [1,2,3], k = 3
Output: 2

```

 

 **Constraints:** 

- 1 <= nums.length <= 2 * 104
- -1000 <= nums[i] <= 1000
- -107 <= k <= 107

## Solution

**Language:** Python  
**Runtime:** 35 ms (beats 46.28%)  
**Memory:** 21.9 MB (beats 56.55%)  
**Submitted:** 2026-09-04T09:46:13.675Z  

```py
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        freq = {0:1}
        count = 0
        sum = 0
        n = len(nums)
        for idx in range(n):
            sum += nums[idx]
            target = sum - k
            if target in freq:
                count += freq.get(target, 0)
            freq[sum] = freq.get(sum, 0) + 1
        return count
```

---

[View on LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/)