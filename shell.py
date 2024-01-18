from lexer import lexer
from parser import Parser
from interpreter import Interpreter
from data import Data 

base = Data()

print("Falcon 1.0.0(default)\nOn linux\nreach out to me at who knows..lol\nCREATED BY WISDOM\n")



while True:
    text = input(">>>")

    tokenizer = lexer(text)
    tokens = tokenizer.tokenize()

    parser = Parser(tokens)
    tree = parser.parse()

    interpreter = Interpreter(tree,base)
    result = interpreter.interpret()
    if result is not None:
        print(result)

    

    
