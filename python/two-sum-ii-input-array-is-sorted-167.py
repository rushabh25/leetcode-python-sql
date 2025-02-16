class Problem167:
    def twosum(self, nums: list[int], target: int):
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left+1, right+1]
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return []


