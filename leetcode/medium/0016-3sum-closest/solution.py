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