class Solution:
    def countPrimes(self, n: int) -> int:
        counter = 0
        def isPrime(num: int) -> bool:
            if num <= 1:
                return False
            elif num == 2 or num == 3:
                return True
            elif num % 2 == 0 or num % 3 == 0 or num == 4:
                return False
            else:
                for i in range(5, (num // 2) + 1, 2):
                    if num % i == 0:
                        return False
            return True

        for x in range(n):
            if isPrime(x):
                print(x)
                counter += 1
        return counter