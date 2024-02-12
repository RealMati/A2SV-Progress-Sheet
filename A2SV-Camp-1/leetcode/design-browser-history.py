class Page:
    def __init__(self,url):
        self.forward=None
        self.url=url
        self.back=None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur=Page(homepage)

    def visit(self, url: str) -> None:
        newPage=Page(url)
        self.cur.forward=newPage
        newPage.back=self.cur
        self.cur=self.cur.forward
        # print("v",self.cur.url)

    def back(self, steps: int) -> str:        
        s=0
        
        while self.cur.back and s<steps:
            self.cur=self.cur.back
            s+=1

        # print("b",self.cur.url)
        return self.cur.url

    def forward(self, steps: int) -> str:
        s=0
        
        while self.cur.forward and s<steps:
            self.cur=self.cur.forward
            s+=1

        # print(self.cur.url)
        return self.cur.url



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)