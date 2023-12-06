class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

            
        if num1=="0" or num2=="0":
            return "0"
        number1=dic[num1[0]]
        number2=dic[num2[0]]
        index=1
        while index<len(num1) or index<len(num2):
            if index<len(num1):
                n=dic[num1[index]]
                number1=(number1*10)+n
            if index<len(num2):
                nn=dic[num2[index]]
                number2=(number2*10)+nn
        
            index+=1
        return str(number1*number2)
        

            