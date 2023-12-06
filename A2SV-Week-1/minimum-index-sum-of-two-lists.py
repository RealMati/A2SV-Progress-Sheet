class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]: 

        
        index_list=[]
        index1={}
        for i,word1 in enumerate(list1):
            index1[word1]=i


        for j,word2 in enumerate(list2):
            if word2 in index1:
                index_list.append([word2,index1[word2]+j])
        index_list=sorted(index_list, key=lambda x:x[1])
        minimum_sum=index_list[0][1]
        for i,item in enumerate(index_list):
            if item[1]!=minimum_sum:
                index_list=index_list[:i]
                break
            else:
                index_list[i]=item[0]
        return index_list

    
        