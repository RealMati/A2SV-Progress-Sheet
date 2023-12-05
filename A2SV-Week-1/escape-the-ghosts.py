class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
            
        cur_pos=[0,0]
        
        for ghost in range(len(ghosts)):
            ghost_move=0
            while ghosts[ghost]!=target:
                
                if ghosts[ghost][0]>target[0]:
                    ghosts[ghost][0]-=1
                    ghost_move+=1
                elif ghosts[ghost][1]>target[1]:
                    ghosts[ghost][1]-=1
                    ghost_move+=1
                elif ghosts[ghost][0]<target[0]:
                    ghosts[ghost][0]+=1
                    ghost_move+=1
                elif ghosts[ghost][1]<target[1]:
                    ghosts[ghost][1]+=1
                    ghost_move+=1
            
            ghosts[ghost]=ghost_move
        user_move=0
        while cur_pos!=target:
            if cur_pos[0]<target[0]:
                cur_pos[0]+=1
                user_move+=1
            elif cur_pos[1]<target[1]:
                cur_pos[1]+=1
                user_move+=1
            elif cur_pos[0]>target[0]:
                cur_pos[0]-=1
                user_move+=1
            elif cur_pos[1]>target[1]:
                cur_pos[1]-=1
                user_move+=1
        ghosts.sort()
        if user_move<ghosts[0]:
            return True
        else:
            return False

