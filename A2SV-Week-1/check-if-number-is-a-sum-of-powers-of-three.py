class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n!=1:
            if n%3==2:
                return False
            else:
                n=n//3

        return True