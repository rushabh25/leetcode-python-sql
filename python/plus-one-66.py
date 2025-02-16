###
# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
###
from collections import deque
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        d = deque()
        plusOne = 1
        for i in range(len(digits)-1, -1, -1):
            sum = plusOne + digits[i]
            if sum < 10:
                plusOne = 0
            else:
                plusOne = 1
            rem = sum % 10
            d.appendleft(rem)
        if plusOne == 1:
            d.appendleft(1)
        return list(d)
