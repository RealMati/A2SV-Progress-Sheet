class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k<=numOnes:
            return k
        elif numOnes+numZeros>=k>numOnes:
            return numOnes
        else:
            return numOnes-(k-(numOnes+numZeros))
        