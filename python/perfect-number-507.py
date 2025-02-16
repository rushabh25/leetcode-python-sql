class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 0
        list = []
        for i in range(1, num//2 +1):
            if num % i == 0:
                list.append(i)
        print(list)
        for n in list:
            sum += n
        return sum == num
