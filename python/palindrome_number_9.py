class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        temp = x
        reverse_num = 0
        while temp != 0:
            quot = temp // 10
            rem = temp % 10
            reverse_num = reverse_num * 10 + rem
            temp = quot
        return reverse_num == x


