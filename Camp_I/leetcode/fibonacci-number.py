class Solution:
    def __init__(self):
        self.visited = {}
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n in self.visited:
            return self.visited[n]
        first = self.fib(n-1)
        second = self.fib(n-2)
        self.visited[n] = first+second
        return first + second