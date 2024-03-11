class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=y=0
        for move in moves:
            if move=="U":
                y+=1
            elif move=='D':
                y-=1
            elif move=='L':
                x-=1
            else:
                x+=1
                
        if y==x and x==0:
            return True
        return False