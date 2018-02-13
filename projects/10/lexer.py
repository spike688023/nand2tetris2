import sys,os
import string

def RemoveComments( OriginFile ):
    RemoveComments = Orign_file[:-5] + 'RemoveComments.xml'
    writtenFile = open(RemoveComments,'w')
    jackfile = open( OriginFile,'r' )
    # delete comments
    lines = jackfile.read().splitlines()
    commentsBlock = False
    for i in lines:
        list1 = i.split()
        onlycomments = False
        if len(list1) > 0 and "//" in list1[0]: onlycomments = True
        if "/*" in i:
            commentsBlock = True
            if "*/" in i:
                commentsBlock = False
                continue
            continue
        if commentsBlock and "*/" in i:
            commentsBlock = False
            continue
        elif  commentsBlock and "*/" not in i:
            continue
        index = i.find("//")
        if len(list1) > 0 and index < 0 :
            writtenFile.write( i + "\n")
        elif len(list1) > 0 and index > 0 and onlycomments == False:
            writtenFile.write( i[0:index] + "\n")
    writtenFile.close()
    jackfile.close()
    return RemoveComments

def Tokenize( RemoveFileName , TokenFileName):
    File = open(RemoveFileName,'r')
    File2 = open(TokenFileName,'w')
    content = File.read()
    lexer = Lexer(content, File2)
    for token in lexer.tokenise():
        #print token
        token.writeToFile()
    File.close()
    File2.close()
    os.remove(RemoveFileName)
    return lexer.tokenise()

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
            if self.value == "<":
                 self.value = "&lt;"
            elif self.value == ">":
                 self.value = "&gt;"
            elif self.value == '"':
                 self.value = "&quot;"
            elif self.value == "&":
                 self.value = "&amp;"
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
            else:
                raise ValueError('Unexpected character found: {0}:{1} -> {2}\n{3}'.format(self.line_no + 1, self.line_pos + 1, char, self.lines[self.line_no]))

        # end of file token
        token = Token(Token.eof, char, None, self.line_no, self.line_pos, self.file2)
        self.tokens.append(token)

        return self.tokens

class Tokenizer():
    def __init__(self, tokens):
        self.index = 0

    def printAllTokens(self):
        for token in tokens:
            print token

    def hasMoreTokens(self):
        if self.index + 1 < len(tokens):
            return True
        else:
            return False

    def advance(self):
        if self.index + 1 < len(tokens):
            self.index = self.index + 1

    def backOneToken(self):
        if self.index - 1 >= 0:
            self.index = self.index - 1

    def tokenType(self):
        return tokens[self.index].type

    def keyWord(self):
        if tokens[self.index].type == "keyword":
            return tokens[self.index].value
        else:
            return "wrong token Type"

    def symbol(self):
        if tokens[self.index].type == "symbol":
            return tokens[self.index].value
        else:
            return "wrong token Type"

    def identifier(self):
        if tokens[self.index].type == "identifier":
            return tokens[self.index].value
        else:
            return "wrong token Type"

    def intVal(self):
        if tokens[self.index].type == "integerConstant":
            return tokens[self.index].value
        else:
            return "wrong token Type"

    def stringVal(self):
        if tokens[self.index].type == "stringConstant":
            return tokens[self.index].value
        else:
            return "wrong token Type"


class CompilationEngine():

    def __init__(self, tokenizer, file):
        self.tokenizer = tokenizer
        self.file = open(file,'w')
        self.level = 0

    def mainEngine(self):
        while self.tokenizer.hasMoreTokens():
            #self.file.write("test" + "\n")
            if self.tokenizer.tokenType() == "keyword":
                #print "out tokenType() = " + self.tokenizer.tokenType()
                if self.tokenizer.keyWord() == "class":
                    self.compileClass()
            self.tokenizer.advance()

    def writePattern(self, type , value, level):
        #str =
        self.file.write( (' ' * level * 2) + "<" + type  + "> " + value  + " </" + type + ">" + "\n")

    def compileClass(self):
        self.file.write("<class>" + "\n")
        self.level = self.level + 1
        # class
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , self.level)

        # className
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , self.level)

        # {  symbol
        self.tokenizer.advance()
        if self.tokenizer.tokenType() == "symbol" and self.tokenizer.symbol() == "{":
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , self.level)
        self.tokenizer.advance()

        # ClassVarDec
        if self.tokenizer.tokenType() == "keyword" and self.tokenizer.keyWord() in [ "static", "field"]:
            while self.tokenizer.tokenType() == "keyword" and self.tokenizer.keyWord() in [ "static", "field"]:
                self.compileClassVarDec(self.level)
                self.tokenizer.advance()

        # subRoutineDec
        while self.tokenizer.keyWord() in [ "constructor", "function", "method"]:
            self.compileSubroutine(self.level)
            self.tokenizer.advance()

        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() ,self. level)
        self.file.write("</class>" + "\n")

    def compileClassVarDec(self, level):

        self.file.write( ( ' ' * level * 2) + "<classVarDec>" + "\n")
        level = level + 1
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)

        # type
        self.tokenizer.advance()
        if self.tokenizer.keyWord() in [ "int", "char", "boolean"]:
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
        else:
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

        # VarName
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

        # (',' varName)* ','
        self.tokenizer.advance()
        while  self.tokenizer.tokenType() == "symbol" and self.tokenizer.symbol() == ',':
            # , symbol
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            #  VarName
            self.tokenizer.advance()
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

            #  Get next token
            self.tokenizer.advance()
        # end of declation , and the end of symbol is ;
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</classVarDec>" + "\n")

    def compileSubroutine(self, level):
        self.file.write( ( ' ' * level * 2) + "<subroutineDec>" + "\n")
        level = level + 1

        # constructor, function, method
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
        # ('void' | type)
        self.tokenizer.advance()
        if self.tokenizer.keyWord() in [ "int", "char", "boolean", "void"]:
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
        else:
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

        # subroutineName
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

        # '('
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

        #  parameterList = ( (type varName) (',' type varName)*)?
        self.tokenizer.advance()
        if self.tokenizer.symbol() != ')':
            self.compileParameterList(level)
        else:
            self.file.write( ( ' ' * level * 2) + "<parameterList>" + "\n")
            self.file.write( ( ' ' * level * 2) + "</parameterList>" + "\n")
        # ')'
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

        #  subroutineBody = '{' varDec* statements '}'
        self.file.write( ( ' ' * level * 2) + "<subroutineBody>" + "\n")
        #  '{'
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

        # varDec* = 'var' type varName ( ','varName)*';'
        self.tokenizer.advance()
        while self.tokenizer.keyWord() == "var" :
            self.compileVarDec(level)
            self.tokenizer.advance()

        # statements
        self.tokenizer.backOneToken()
        self.compileStatements(level)

        #  '}'
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        self.file.write( ( ' ' * level * 2) + "</subroutineBody>" + "\n")

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</subroutineDec>" + "\n")

    #  parameterList = ( (type varName) (',' type varName)*)?
    def compileParameterList(self, level):
        self.file.write( ( ' ' * level * 2) + "<parameterList>" + "\n")
        level = level + 1

        # type = 'int' | 'char' | 'boolean' | className
        if self.tokenizer.keyWord() in ["int", "char", "boolean"]:
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
        else:
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

        # varName
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

        #  (',' type varName)*
        self.tokenizer.advance()
        while self.tokenizer.symbol() == ',':
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            # type = 'int' | 'char' | 'boolean' | className
            self.tokenizer.advance()
            if self.tokenizer.keyWord() in ["int", "char", "boolean"]:
                self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
            else:
                self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

            # varName
            self.tokenizer.advance()
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

            self.tokenizer.advance()

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</parameterList>" + "\n")

    # varDec* = 'var' type varName ( ','varName)*';'
    def compileVarDec(self, level):
        self.file.write( ( ' ' * level * 2) + "<varDec>" + "\n")
        level = level + 1

        # 'var'
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)

        # type
        # type = 'int' | 'char' | 'boolean' | className
        self.tokenizer.advance()
        if self.tokenizer.keyWord() in ["int", "char", "boolean"]:
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
        else:
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)


        # varName
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)


        #  (',' varName)*;
        self.tokenizer.advance()
        while self.tokenizer.symbol() == ',':
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            # varName
            self.tokenizer.advance()
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

            self.tokenizer.advance()
        #  ;
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</varDec>" + "\n")

    def compileStatements(self, level):
        self.tokenizer.advance()
        self.file.write( ( ' ' * level * 2) + "<statements>" + "\n")
        while self.tokenizer.keyWord() in ["let", "if", "while", "do", "return"] :
            if self.tokenizer.keyWord() == "let":
                self.compileLet(level)
            elif self.tokenizer.keyWord() == "if":
                self.compileIf(level)
            elif self.tokenizer.keyWord() == "while":
                self.compileWhile(level)
            elif self.tokenizer.keyWord() == "do":
                self.compileDo(level)
            elif self.tokenizer.keyWord() == "return":
                self.compileReturn(level)
            self.tokenizer.advance()
        self.file.write( ( ' ' * level * 2) + "</statements>" + "\n")

    def compileLet(self, level):
        level = level + 1
        self.file.write( ( ' ' * level * 2) + "<letStatement>" + "\n")

        level = level + 1

        # "let"
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
        # varName
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

        # ('[' experssion ']')? '='
        self.tokenizer.advance()
        if self.tokenizer.symbol() == '[' :
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            # Expression
            self.compileExpression(level)

            # ']'
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            # '='
            self.tokenizer.advance()
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        else:
            # '='
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

        # Expression
        self.compileExpression(level)

        # ';'
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</letStatement>" + "\n")

    def compileDo(self, level):
        self.file.write( ( ' ' * level * 2) + "<doStatement>" + "\n")
        level = level + 1

        # Do
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)

        # subroutinName
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

        self.subroutineCall(level)

        # ';'
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</doStatement>" + "\n")

    def compileWhile(self, level):
        self.file.write( ( ' ' * level * 2) + "<whileStatement>" + "\n")
        level = level + 1

        # While
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)

        # '('
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        level = level + 1
        self.compileExpression(level)

        # ')'
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        # '{'
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        # statements = statement*
        self.compileStatements(level)

        # '}'
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</whileStatement>" + "\n")

    def compileReturn(self, level):
        self.file.write( ( ' ' * level * 2) + "<returnStatement>" + "\n")
        level = level + 1

        # return
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)

        # ;
        self.tokenizer.advance()
        if self.tokenizer.symbol() == ';':
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        else:
            # expression?
            self.tokenizer.backOneToken()
            self.compileExpression(level)
            # ;
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</returnStatement>" + "\n")

    def compileIf(self, level):
        self.file.write( ( ' ' * level * 2) + "<ifStatement>" + "\n")
        level = level + 1

        # If
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)

        # '('
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        level = level + 1
        self.compileExpression(level)

        # ')'
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        # '{'
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        # statements
        self.compileStatements(level)

        # '}'
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

        # ( 'else' '{' statements '}' )?
        self.tokenizer.advance()
        if self.tokenizer.keyWord() == "else":
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
            # '{'
            self.tokenizer.advance()
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            level = level + 1
            self.compileStatements(level)

            # '}'
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        else:
            self.tokenizer.backOneToken()

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</ifStatement>" + "\n")

    def compileExpression(self, level):
        self.file.write( ( ' ' * level * 2) + "<expression>" + "\n")

        # term
        level = level + 1
	# this function will move token ahead
	self.compileTerm(level)

        # (op term)*
        while self.tokenizer.symbol() in [ '+', '-', '*', '/', '&', '|', '&lt;', '&gt;', '=' , '&amp;']:

            # op
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

            # term
	    self.compileTerm(level)

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</expression>" + "\n")

    def compileTerm(self, level):

        self.file.write( ( ' ' * level * 2) + "<term>" + "\n")
        self.tokenizer.advance()

        # integerConstant | stringConstant | keywordConstant
        if self.tokenizer.tokenType() in [ "integerConstant", "stringConstant" ]:
	    if self.tokenizer.tokenType() ==  "integerConstant":
	        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.intVal() , level)
	    elif self.tokenizer.tokenType() ==  "stringConstant":
	        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.stringVal() , level)
	    # keep while loop works fine
	    self.tokenizer.advance()

        # keywordConstant = true | false | null | this
        elif self.tokenizer.keyWord() in [ 'true', 'false', 'null', 'this']:
	    self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
	    # keep while loop works fine
	    self.tokenizer.advance()

        # varName | varName '[' expression ']' | subroutineCall
        elif self.tokenizer.tokenType() ==  "identifier" :
	    # varName
	    self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

	    self.tokenizer.advance()
	    # '['
	    if self.tokenizer.symbol() == '[' :
	        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
	        # expression
	        self.compileExpression(level)
	        # ']'
	        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
	        # keep while loop works fine
	        self.tokenizer.advance()
            elif self.tokenizer.symbol() in [ "(", "." ]:
                # subroutineCall
	        self.tokenizer.backOneToken()
	        self.subroutineCall(level)
	        # keep while loop works fine
	        self.tokenizer.advance()

        # '(' expression ')'
        elif self.tokenizer.symbol() == '(':
	    # '('
	    self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
	    # expression
	    self.compileExpression(level)

	    # ')'
    	    self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

	    # keep while loop works fine
	    self.tokenizer.advance()
        # unaryOp term
        # not come to this condition twice
        elif self.tokenizer.symbol() in ['-','~']:
	    # unaryOp
	    self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
	    self.compileTerm(level)
        self.file.write( ( ' ' * level * 2) + "</term>" + "\n")

    def compileExpressionList(self, level):
        self.file.write( ( ' ' * level * 2) + "<expressionList>" + "\n")
        level = level + 1

        self.tokenizer.advance()
        # ( expression ( ','expression )* )?
        if self.tokenizer.symbol() != ")":
            # expression
            self.tokenizer.backOneToken()
            self.compileExpression(level)

            # ( ','expression )*
            while self.tokenizer.symbol() == ',':
                # ','
                self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
                self.compileExpression(level)

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</expressionList>" + "\n")

    def subroutineCall(self, level):

        # '(' or '.'
        self.tokenizer.advance()
        if self.tokenizer.symbol() == '(':
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            self.compileExpressionList(level)

            # ')'
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

        elif self.tokenizer.symbol() == '.':
            # '.'
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            # subroutineName
            self.tokenizer.advance()
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

            # '('
            self.tokenizer.advance()
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            # ExpressionList
            self.compileExpressionList(level)

            # ')'
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

if  __name__ =='__main__':

    listFilePath = sys.argv[1].split('/')
    containJackFile = True
    if ".jack" not in sys.argv[1]:
        containJackFile = False

    RemoveCommentsFile = ''
    if containJackFile == True:
        Orign_file = sys.argv[1]
        TokenFileName = Orign_file[:-5] + 'T.xml'
        FinalFileName = Orign_file[:-5] + '.xml'
        RemoveFileName = RemoveComments( sys.argv[1] )
        tokens = Tokenize( RemoveFileName , TokenFileName)
        tokenizer = Tokenizer(tokens)
        cplEngine = CompilationEngine(tokenizer, FinalFileName)
        cplEngine.mainEngine()
    elif containJackFile == False :
        JackFilelist = [ i for i in os.listdir('/'.join(listFilePath[0:-1])) if ".jack" in i]
        #print JackFilelist
        for i in JackFilelist:
            Orign_file = sys.argv[1] + i
            TokenFileName = Orign_file[:-5] + 'T.xml'
            FinalFileName = Orign_file[:-5] + '.xml'
            RemoveFileName = RemoveComments( sys.argv[1] + i )
            tokens = Tokenize( RemoveFileName , TokenFileName)
            tokenizer = Tokenizer(tokens)
            cplEngine = CompilationEngine(tokenizer, FinalFileName)
            cplEngine.mainEngine()


