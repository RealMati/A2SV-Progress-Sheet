class FrequencyTracker(object):

    def __init__(self):
        self.freq=defaultdict(int)
        self.count=defaultdict(int)
    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        #adds it to frequency
        self.freq[number]+=1

        #removes itfrom the prev grp
        if self.freq[number]-1:
            self.count[self.freq[number]-1]-=1

         #adds it to the prev grp
        self.count[self.freq[number]]+=1


        

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if self.freq[number]:
            self.freq[number]-=1


            #removes it from the prev grp

            self.count[self.freq[number]+1]-=1

            #adds it to the new grp
            self.count[self.freq[number]]+=1
            
            

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        if self.count[frequency]: return True

        return False
        
        


        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)