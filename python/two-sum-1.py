class Problem1:
    def twosum(self, nums: list[int], target: int):
        my_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in my_map:
                return [i, my_map[diff]]
            my_map[nums[i]] = i
        return []

