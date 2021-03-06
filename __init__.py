from lexer.lexer import Lexer
from parser.parser import Parser
from symbole.semantic_analyzer import SemanticAnalyzer

INPUT_FILE = "input/test.txt"

if __name__ == '__main__':
    with open(INPUT_FILE) as f:
        lexer = Lexer(f.read())
        parser = Parser(lexer)
        tree = parser.parse()

        semantic_analyzer = SemanticAnalyzer()
        try:
            semantic_analyzer.visit(tree)
        except Exception as e:
            print(e)
