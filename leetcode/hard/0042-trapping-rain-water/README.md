# Trapping Rain Water

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

 

 **Example 1:** 

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

```

 **Example 2:** 

```
Input: height = [4,2,0,3,2,5]
Output: 9

```

 

 **Constraints:** 

- n == height.length
- 1 <= n <= 2 * 104
- 0 <= height[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 72.01%)  
**Memory:** 21.1 MB (beats 25.49%)  
**Submitted:** 2026-09-21T02:52:07.921Z  

```py
class Solution:
    def trap(self, height: list[int]) -> int:
        # n = len(height)
        # totalwater = 0
        # leftMax = height[0]
        # rightMax = height[n-1]
        # for i in range(n):
        #     for j in range(i+1):
        #         leftMax = max(leftMax, height[j])
            
        #     for j in range(1, n):
        #         rightMax = max(rightMax, height[j])
            
        #     totalwater += min(leftMax, rightMax) - height[i]
        # return totalwater


        # Two Pointer
        n = len(height)
        totalwater = 0

        left = 0
        right = n - 1
        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                totalwater += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                totalwater += rightMax - height[right]
        return totalwater
```

---

[View on LeetCode](https://leetcode.com/problems/trapping-rain-water/)