“””
Reference:
    http://blog.tjwakeham.com/compiler-development-in-python-lexical-analysis-part-2/
“””
import string

class Token(object):
    eof = 'END-OF-FILE'
    ident = 'identifier'
    number = 'integerConstant'
    symbol = 'symbol'
    keyword = 'keyword'
    stringConstant = 'stringConstant'
    #block_start = 'START'
    #block_end = 'END'

    keywords = ['class', 'constructor', 'function', 'method' , 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while','return']

    def __init__(self, type, value, line, line_no, line_pos, file2):
        self.type = type
        self.value = value
        self.line = line
        self.line_pos = line_pos - len(value)
        self.line_no = line_no
        self.file2 = file2

    def __str__(self):
        if self.type == 'END-OF-FILE':
            return  "</tokens>"
        else:
            return '{0} {1} {2}'.format("<" + self.type + ">", self.value ,"</" + self.type + ">")

    def writeToFile(self):
        if self.type == 'END-OF-FILE':
            self.file2.write( "</tokens>" + "\n")
        else:
            self.file2.write('{0} {1} {2}'.format("<" + self.type + ">", self.value ,"</" + self.type + ">") + "\n")

class Lexer(object):

    eof_marker = '$'
    whitespace = ' \t\n'
    newline = '\n'
    comment_marker = '//'

    def __init__(self, code, file2):
        super(Lexer, self).__init__()

        self.code = code
        self.file2 = file2
        self.cursor = 0
        self.tokens = []

        self.lines = code.split(Lexer.newline)
        # row
        self.line_no = 0
        # column
        self.line_pos = 0
        print "<tokens>"
        file2.write( "<tokens>" + "\n")

    def get_next_char(self):
        self.cursor += 1
        self.line_pos += 1
        if self.cursor > len(self.code):
            return Lexer.eof_marker

        return self.code[self.cursor - 1]

    def tokenise(self):
        char = self.get_next_char()
        while char != Lexer.eof_marker:

            # ignore whitespace
            if char in Lexer.whitespace:
                if char in Lexer.newline:
                    self.line_no += 1
                    self.line_pos = 0
                char = self.get_next_char()

            # comment
           #elif char in Lexer.comment_marker:
           #    while char not in Lexer.newline:
           #        char = self.get_next_char()

            # StringConstant token
            elif char in ( '"' ):
                match = char
                char = self.get_next_char()
                while char not in ( '"' ) :
                    match += char
                    char = self.get_next_char()
                char = self.get_next_char()
                token = Token(Token.ident, match[1:], self.lines[self.line_no], self.line_no, self.line_pos, self.file2)
                token.type = Token.stringConstant
                self.tokens.append(token)


            # identifier token
            elif char in ( string.ascii_letters + '_' ):
                match = char
                char = self.get_next_char()
                while char in (string.ascii_letters + '_' + string.digits):
                    match += char
                    char = self.get_next_char()
                token = Token(Token.ident, match, self.lines[self.line_no], self.line_no, self.line_pos, self.file2)

                if match in Token.keywords:
                    token.type = Token.keyword

                self.tokens.append(token)

            # number token
            elif char in string.digits:
                match = char
                char = self.get_next_char()
                while char in string.digits:
                    match += char
                    char = self.get_next_char()

                token = Token(Token.number, match, self.lines[self.line_no], self.line_no, self.line_pos, self.file2)
                self.tokens.append(token)

            # symbols
            elif char in '{}()[].,;+-*/&|<>=~':
                token = Token(Token.symbol, char, self.lines[self.line_no], self.line_no, self.line_pos, self.file2)
                self.tokens.append(token)
                char = self.get_next_char()

          ### start block
          ##elif char == '{':
          ##    token = Token(Token.block_start, char, self.lines[self.line_no], self.line_no, self.line_pos)
          ##    self.tokens.append(token)
          ##    char = self.get_next_char()

          ### end block
          ##elif char == '}':
          ##    token = Token(Token.block_end, char, self.lines[self.line_no], self.line_no, self.line_pos)
          ##    self.tokens.append(token)
          ##    char = self.get_next_char()

            else:
                raise ValueError('Unexpected character found: {0}:{1} -> {2}\n{3}'.format(self.line_no + 1, self.line_pos + 1, char, self.lines[self.line_no]))

        # end of file token
        token = Token(Token.eof, char, None, self.line_no, self.line_pos, self.file2)
        self.tokens.append(token)

        return self.tokens

if  __name__ =='__main__':
    File = open("Main.jack",'r')
    File2 = open("MainT.xml",'w')
    content = File.read()
    lexer = Lexer(content, File2)
    for token in lexer.tokenise():
        print token
        token.writeToFile()
    File.close()
    File2.close()
