class AuthenticationManager(object):

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.timeToLive=timeToLive
        self.startTime={}
        self.endTime={}
        

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self.startTime[tokenId]=currentTime
        self.endTime[tokenId]=currentTime+self.timeToLive
        

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if tokenId in self.endTime and self.endTime[tokenId]>currentTime:
            self.startTime[tokenId]=currentTime
            self.endTime[tokenId]=currentTime+self.timeToLive

            

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        ct=0
        for end in self.endTime.values():
            if end>currentTime:
                ct+=1
        return ct
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)