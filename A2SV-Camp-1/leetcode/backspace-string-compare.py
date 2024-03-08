class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss=[]
        tt=[]

        for ch in s:
            if ch=='#': 
                if ss:
                    ss.pop()
                continue
            ss.append(ch)

        for ch in t:
            if ch=='#': 
                if tt:
                    tt.pop()
                continue
            tt.append(ch)
        # print(ss, tt)
        return ss==tt
            