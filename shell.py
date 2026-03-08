from lexer import Lexer
while True:
    text=input("Volt: ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    print(tokens)