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