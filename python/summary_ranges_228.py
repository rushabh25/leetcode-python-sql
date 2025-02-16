

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        initial_index = 0
        list = []
        if len(nums) == 0: return []
        if len(nums) == 1: return [str(nums[0])]
        diff = False

        for curr_index in range(1, len(nums)):
            if nums[curr_index] - nums[curr_index-1] == 1:
                diff = True
            else:
                diff = False

            if not diff:
                if curr_index - initial_index >= 2:
                    list.append(str(nums[initial_index]) + "->" + str(nums[curr_index-1]))
                    initial_index = curr_index
                else:
                    list.append(str(nums[initial_index]))
                    initial_index = curr_index

        if len(nums) - initial_index > 1:
            list.append(str(nums[initial_index]) + "->" + str(nums[len(nums) - 1]))
        else:
            list.append(str(nums[initial_index]))

        return list





