from tokens import Float,Integer,Operation,Declaration,Variable,Boolean,Comprasion,Reserved

class lexer:

    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    operations = "+-/*()="
    stopwords = [" "]
    declarations = ["set"]
    boolean = ["and", "or", "not"]
    comprasions = [">", "<", ">=" , "<=" "?="]
    specialCharacters = "><=?"
    reserved = ["if", "elif" , "else" , "do","while"]

    def __init__(self,text):
        self.text = text
        self.idx = 0
        self.tokens = []
        self.char = self.text[self.idx]
        self.token = None
     

    def tokenize (self):
        while self.idx < len(self.text):
            if self.char in lexer.digits:
                self.token = self.extract_number()

            elif self.char in lexer.operations:
                self.token = Operation(self.char)
                self.move()

            elif self.char in lexer.stopwords:
                self.move()
                continue

            elif self.char in lexer.letters:
                word = self.extract_word()

                if word in lexer.declarations:
                    self.token = Declaration(word)

                elif word in lexer.boolean:
                    self.token = Boolean(word)
                elif word in lexer.reserved:
                    self.token = Reserved(word)

                else:
                    self.token = Variable(word)


            elif  self.char in lexer.specialCharacters:
                comprasionOperator = ""
                while self.char in lexer.specialCharacters and self.idx < len(self.text):
                    comprasionOperator += self.char
                    self.move()

                self.token = Comprasion(comprasionOperator)


            self.tokens.append(self.token)

        return self.tokens

    def extract_number (self):
        number = ""
        isFloat = False
        while(self.char in lexer.digits or self.char == ".") and (self.idx < len(self.text)):
            if self.char == ".":
                isFloat = True
            number += self.char
            self.move()

        #return integer(number) if not isFloat else float(number)
        return Integer(number) if not isFloat else Float(number)

    def extract_word(self):
        word = ""
        while self.char in lexer.letters and self.idx < len(self.text):
            word += self.char
            self.move()

        return word


    def move (self):
        self.idx +=1
        if self.idx < len(self.text):
            self.char = self.text[self.idx]


        