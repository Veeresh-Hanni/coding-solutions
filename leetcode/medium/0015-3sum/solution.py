class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # result = set()
        # n = len(nums)
        # for i in range(n-2):
        #     for j in range(i+1, n-1):
        #         for k in range(j+1, n):
        #             if ((nums[i] + nums[j] + nums[k]) == 0):
        #                result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        # return [list(x) for x in result]

        nums.sort()

        result = []
        n = len(nums)

        for i in range(n - 2):

            # skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:

                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # skip duplicate j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # skip duplicate k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif total < 0:
                    j += 1

                else:
                    k -= 1

        return result
