class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.index = 0
        self.count = 0
        self.char = ''

    def next(self) -> str:
        if not self.hasNext():
            return " "
        self.count -= 1
        return self.char
       
        

    def hasNext(self) -> bool:
        if self.count == 0 and self.index < len(self.s):
            self.char = self.s[self.index]
            self.index += 1

            numstr = ""
            while self.index < len(self.s) and self.s[self.index].isdigit():
                numstr += self.s[self.index]
                self.index += 1

            self.count = int(numstr)
        return self.count > 0
        
        
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
