class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows=["qwertyuiop","asdfghjkl","zxcvbnm"]
        res=[]
        for word in words:
            same=True
            for row in rows:
                if word[0].lower() in row:
                    for letter in word:
                        l=letter.lower()
                        if l not in row:
                            same=False
                            break
                    if same:
                        res.append(word)    
                    break
        return res
