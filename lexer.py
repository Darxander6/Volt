from tokens import Integer,Float,Operation

class Lexer:
    digits= "0123456789"
    operations = "+-/*()="
    stopwords = [" "]
    declarations = ["create"]
    boolean = ["and", "or", "not"]
    comparisons = [">", "<", ">=", "<=", "?="]
    specialCharacters = "><=?"
    reserved = ["if", "elif", "else", "do", "while"]
    def __init__(self,text):
        self.text=text
        self.idx=0
        self.tokens=[]
        self.char=self.text[self.idx]
        self.token=None
    def tokenize(self):
        while self.idx<len(self.text):
            if self.char in Lexer.digits:
                self.token=self.extract_number()
            elif self.char in Lexer.operations:
                self.token= Operation(self.char)
                self.move()
            elif self.char in Lexer.stopwords:
                self.move()
                continue
            self.tokens.append(self.token)
        return self.tokens
    def extract_number(self):
        
        number = ""
        isFloat=False
        
        while (self.char in Lexer.digits or self.char==".") and (self.idx < len(self.text)):
            if self.char == ".":
                isFloat=True
            number += self.char
            self.move()
        if not isFloat:
            return Integer(number)
        else:
            return Float(number)
            
    def move(self):
        self.idx+=1
        if self.idx <len(self.text):
            self.char= self.text[self.idx]
lexer=Lexer("5 + 3")