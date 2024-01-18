class token:
    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __repr__(self):
        return str(self.value)
        

class Integer(token):
    def __init__(self,value ):
        super().__init__("INT",value)

class Float(token):
    def __init__(self,value ):
        super().__init__("FLT",value)

class Operation(token):
    def __init__ (self, value):
        super().__init__("OP", value)

class Declaration(token):
     def __init__ (self, value):
        super().__init__("DECL", value)

class Variable(token):
     def __init__ (self, value):
        super().__init__("VAR(?)", value)

class Boolean(token):
     def __init__ (self, value):
        super().__init__("BOOL", value)

class Comprasion(token):
     def __init__ (self, value):
        super().__init__("COMP", value)

class Reserved(token):
     def __init__ (self, value):
        super().__init__("RSV", value)
