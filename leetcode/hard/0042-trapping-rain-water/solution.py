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