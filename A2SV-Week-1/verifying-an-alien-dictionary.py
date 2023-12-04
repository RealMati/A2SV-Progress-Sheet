class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        word=0
        while word<len(words)-1:
            letter=0
            while letter<len(words[word]) and letter<len(words[word+1]):    
                if order.index(words[word][letter]) < order.index(words[word+1][letter]):       
                    break
                elif order.index(words[word][letter]) == order.index(words[word+1][letter]):
                    letter+=1
                else:
                    return False
            if letter<len(words[word]) and letter>=len(words[word+1]): 
                return False
            else:
                word+=1 
        return True
        