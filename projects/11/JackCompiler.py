import sys,os
import string

opCommand = { '+':"add" , '*':"call Math.multiply 2" , '-':"sub", '/':"call Math.divide 2", '&':"and", '|':"or", '&amp;':"and", '&lt;':"lt" , '&gt;':"gt", '=':"eq"}


def FindTable_And_MemorySegment( symbolTables , fileVm, tableName, action, LocalVariable):
    fount = False
    for i in symbolTables:
        if i.GetTableName() == tableName:
            if i.KindOf(LocalVariable) != "nothing":
                fileVm.write( action + " " +  i.KindOf(LocalVariable) + ' ' + str(i.IndexOf(LocalVariable) ) + "\n")
            else:
                fileVm.write( action + " this" + ' ' + str(symbolTables[0].IndexOf(LocalVariable) ) + "\n")
            break

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

    def __init__(self, tokenizer, file, fileVm):
        self.tokenizer = tokenizer
        self.file = open(file,'w')
        self.fileVm = open(fileVm,'w')
        self.level = 0
        self.currentClassName = ""
        self.currentFunctionName = ""
        self.functionReturnType = ""
        self.dofunctionName = ""
        self.dofunctionParameterCount = 0
        self.symbolTables = []
        self.whileCount = -1
        self.ifCount = -1
        self.functionType = ""

    def GetCurrentTableName(self):
        return self.currentClassName + '_' + self.currentFunctionName

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
        self.currentClassName = self.tokenizer.identifier()

        # {  symbol
        self.tokenizer.advance()
        if self.tokenizer.tokenType() == "symbol" and self.tokenizer.symbol() == "{":
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , self.level)
        self.tokenizer.advance()

        # ClassVarDec
        classSymbolTable = SymbolTable( self.currentClassName )
        self.symbolTables.append( classSymbolTable )
        if self.tokenizer.tokenType() == "keyword" and self.tokenizer.keyWord() in [ "static", "field"]:
            while self.tokenizer.tokenType() == "keyword" and self.tokenizer.keyWord() in [ "static", "field"]:
                self.compileClassVarDec(self.level, classSymbolTable)
                self.tokenizer.advance()

        #self.symbolTables[0].PrintAll()

        # subRoutineDec
        while self.tokenizer.keyWord() in [ "constructor", "function", "method"]:
            self.compileSubroutine(self.level)
            self.tokenizer.advance()

        # }
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() ,self. level)
        self.file.write("</class>" + "\n")

        # print all symbol tables
        for i in self.symbolTables:
            i.PrintAll()

    def compileClassVarDec(self, level, table):

        kind = ""
        type = ""
        name = ""

        self.file.write( ( ' ' * level * 2) + "<classVarDec>" + "\n")
        level = level + 1
        # kind = [static , field]
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
        kind = self.tokenizer.keyWord()

        # type
        self.tokenizer.advance()
        if self.tokenizer.keyWord() in [ "int", "char", "boolean"]:
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
            type = self.tokenizer.keyWord()
        else:
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)
            type = self.tokenizer.identifier()

        # VarName
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)
        name = self.tokenizer.identifier()
        table.define( name, type, kind )


        # (',' varName)* ','
        self.tokenizer.advance()
        while  self.tokenizer.tokenType() == "symbol" and self.tokenizer.symbol() == ',':
            # , symbol
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            #  VarName
            self.tokenizer.advance()
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)
            name = self.tokenizer.identifier()
            table.define( name, type, kind )

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
        self.functionType = self.tokenizer.keyWord()

        # "this" is the fist argument if type of function is method
        if self.functionType == "method":
            self.symbolTables[-1].define( "this", self.currentClassName , "argument")

        # ('void' | type)
        self.tokenizer.advance()
        if self.tokenizer.keyWord() in [ "int", "char", "boolean", "void"]:
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
            self.functionReturnType = self.tokenizer.keyWord()
        # type
        else:
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)
            self.functionReturnType = self.tokenizer.keyWord()

        # subroutineName
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

        self.currentFunctionName = self.tokenizer.identifier()
        subroutinSymbolTable = SymbolTable( self.currentClassName + '_' + self.currentFunctionName  )
        self.symbolTables.append( subroutinSymbolTable )

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

        self.fileVm.write( "function " + self.currentClassName + '.' +  self.currentFunctionName + ' ' + str(self.symbolTables[-1].GetVarCount("local") + 1) + "\n")

        # check the first symbol table to get how many field variables
        if self.functionType  == "constructor":
            self.fileVm.write( "push constant " + str(self.symbolTables[0].GetVarCount("field") + 1) + "\n")
            self.fileVm.write( "call Memory.alloc 1" + "\n")
            self.fileVm.write( "pop pointer 0" + "\n")
        elif self.functionType  == "method":
            self.fileVm.write( "push argument 0" + "\n")
            self.fileVm.write( "pop pointer 0" + "\n")

        # statements
        self.tokenizer.backOneToken()
        self.resetStatementsCount()
        self.compileStatements(level)

        #  '}'
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        self.file.write( ( ' ' * level * 2) + "</subroutineBody>" + "\n")

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</subroutineDec>" + "\n")



    #  parameterList = ( (type varName) (',' type varName)*)?
    def compileParameterList(self, level):

        name = ""
        type = ""
        kind = "argument"


        self.file.write( ( ' ' * level * 2) + "<parameterList>" + "\n")
        level = level + 1

        # type = 'int' | 'char' | 'boolean' | className
        if self.tokenizer.keyWord() in ["int", "char", "boolean"]:
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
            type = self.tokenizer.keyWord()
        else:
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)
            type = self.tokenizer.identifier()

        # varName
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)
        name = self.tokenizer.identifier()
        self.symbolTables[-1].define( name , type , kind)

        #  (',' type varName)*
        self.tokenizer.advance()
        while self.tokenizer.symbol() == ',':
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            # type = 'int' | 'char' | 'boolean' | className
            self.tokenizer.advance()
            if self.tokenizer.keyWord() in ["int", "char", "boolean"]:
                self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
                type = self.tokenizer.keyWord()
            else:
                self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)
                type = self.tokenizer.identifier()

            # varName
            self.tokenizer.advance()
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)
            name = self.tokenizer.identifier()
            self.symbolTables[-1].define( name , type , kind)

            self.tokenizer.advance()

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</parameterList>" + "\n")

    # varDec* = 'var' type varName ( ','varName)*';'
    def compileVarDec(self, level):

        name = ""
        type = ""
        kind = "local"

        self.file.write( ( ' ' * level * 2) + "<varDec>" + "\n")
        level = level + 1

        # 'var'
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)

        # type
        # type = 'int' | 'char' | 'boolean' | className
        self.tokenizer.advance()
        if self.tokenizer.keyWord() in ["int", "char", "boolean"]:
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
            type = self.tokenizer.keyWord()
        else:
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)
            type = self.tokenizer.identifier()


        # varName
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)
        name = self.tokenizer.identifier()
        self.symbolTables[-1].define( name, type , kind)


        #  (',' varName)*;
        self.tokenizer.advance()
        while self.tokenizer.symbol() == ',':
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            # varName
            self.tokenizer.advance()
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)
            name = self.tokenizer.identifier()
            self.symbolTables[-1].define( name, type , kind)

            self.tokenizer.advance()
        #  ;
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</varDec>" + "\n")


    def resetStatementsCount(self):
        self.whileCount = -1
        self.ifCount = -1

    def compileStatements(self, level):
        self.tokenizer.advance()
        self.file.write( ( ' ' * level * 2) + "<statements>" + "\n")
        while self.tokenizer.keyWord() in ["let", "if", "while", "do", "return"] :
            if self.tokenizer.keyWord() == "let":
                self.compileLet(level)
            elif self.tokenizer.keyWord() == "if":
                self.ifCount = self.ifCount + 1
                self.compileIf(level, self.ifCount)
            elif self.tokenizer.keyWord() == "while":
                self.whileCount = self.whileCount + 1
                self.compileWhile(level, self.whileCount)
            elif self.tokenizer.keyWord() == "do":
                self.compileDo(level)
            elif self.tokenizer.keyWord() == "return":
                self.compileReturn(level)
            self.tokenizer.advance()
        self.file.write( ( ' ' * level * 2) + "</statements>" + "\n")

    def compileLet(self, level):
        LocalVariable = ""
        case1 = False
        case2 = False
        level = level + 1
        self.file.write( ( ' ' * level * 2) + "<letStatement>" + "\n")

        level = level + 1

        # "let"
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
        # varName
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)
        LocalVariable = self.tokenizer.identifier()


        # ('[' experssion ']')? '='
        self.tokenizer.advance()
        if self.tokenizer.symbol() == '[' :
            case1 = True
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            # Expression
            self.compileExpression(level)

            # ']'
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            FindTable_And_MemorySegment(self.symbolTables , self.fileVm , self.GetCurrentTableName() , "push", LocalVariable)
            self.fileVm.write( "add" + "\n")

            # '='
            self.tokenizer.advance()
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        else:
            case2 = True
            # '='
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

        # Expression
        self.compileExpression(level)

        # ';'
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</letStatement>" + "\n")

        # lookup in symbol tables
        # here depends on left operand ,
        if case2 == True:
            FindTable_And_MemorySegment(self.symbolTables , self.fileVm , self.GetCurrentTableName() , "pop", LocalVariable)
        elif case1 == True:
            self.fileVm.write( "pop temp 0" + "\n")
            self.fileVm.write( "pop pointer 1" + "\n")
            self.fileVm.write( "push temp 0" + "\n")
            self.fileVm.write( "pop that 0" + "\n")

    def compileDo(self, level):
        self.file.write( ( ' ' * level * 2) + "<doStatement>" + "\n")
        level = level + 1

        # Do
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)

        # subroutinName
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)
        # if this subroutineName , could find in symbol table,
        # change the name
        self.dofunctionName = self.tokenizer.identifier()
        # change object name to class name
        if self.symbolTables[-1].VariableExistOrNot( self.dofunctionName ) :
            self.fileVm.write( "push " +  self.symbolTables[-1].KindOf(self.dofunctionName) + ' ' + str(self.symbolTables[-1].IndexOf(self.dofunctionName) ) + "\n")
            self.dofunctionName = self.symbolTables[-1].TypeOf(self.dofunctionName)
            self.dofunctionParameterCount = self.dofunctionParameterCount + 1
        elif self.symbolTables[0].VariableExistOrNot( self.dofunctionName ):
            self.fileVm.write( "push " +  self.symbolTables[0].KindOf(self.dofunctionName) + ' ' + str(self.symbolTables[0].IndexOf(self.dofunctionName) ) + "\n")
            self.dofunctionName = self.symbolTables[0].TypeOf(self.dofunctionName)
            self.dofunctionParameterCount = self.dofunctionParameterCount + 1

        # subroutineCall
        self.subroutineCall(level)
        self.dofunctionName = ""
        # pop out unnecessary data
        self.fileVm.write( "pop temp 0" + "\n")

        # ';'
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</doStatement>" + "\n")

    def compileWhile(self, level, whileCount):
        self.file.write( ( ' ' * level * 2) + "<whileStatement>" + "\n")
        level = level + 1

        # While
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)

        self.fileVm.write( "label WHILE_EXP" + str(whileCount) +  "\n")

        # '('
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        level = level + 1
        self.compileExpression(level)

        self.fileVm.write( "not" +  "\n")

        # ')'
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

        self.fileVm.write( "if-goto WHILE_END" + str(whileCount) +  "\n")

        # '{'
        self.tokenizer.advance()
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        # statements = statement*
        self.compileStatements(level)

        # '}'
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</whileStatement>" + "\n")

        self.fileVm.write( "goto WHILE_EXP" + str(whileCount) +  "\n")
        self.fileVm.write( "label WHILE_END" + str(whileCount) +  "\n")

    def compileReturn(self, level):
        self.file.write( ( ' ' * level * 2) + "<returnStatement>" + "\n")
        level = level + 1

        # return
        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)

        # ;
        self.tokenizer.advance()
        if self.tokenizer.symbol() == ';':
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            self.fileVm.write( "push constant 0" + "\n")

        else:
            # expression?
            self.tokenizer.backOneToken()
            self.compileExpression(level)
            # ;
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
        self.fileVm.write( "return" + "\n")

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</returnStatement>" + "\n")

    def compileIf(self, level, ifCount):
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


        self.fileVm.write( "if-goto IF_TRUE" + str(ifCount) + "\n")
        self.fileVm.write( "goto IF_FALSE" + str(ifCount) + "\n")
        self.fileVm.write( "label IF_TRUE" + str(ifCount) + "\n")
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
            self.fileVm.write( "goto IF_END" + str(ifCount) + "\n")
            self.fileVm.write( "label IF_FALSE" + str(ifCount) + "\n")
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)
            # '{'
            self.tokenizer.advance()
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            level = level + 1
            self.compileStatements(level)

            # '}'
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            self.fileVm.write( "label IF_END" + str(ifCount) + "\n")
        else:
            self.fileVm.write( "label IF_FALSE" + str(ifCount) + "\n")
            self.tokenizer.backOneToken()

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</ifStatement>" + "\n")

    def compileExpression(self, level):
        currentOp = ''
        self.file.write( ( ' ' * level * 2) + "<expression>" + "\n")

        # term
        level = level + 1
	# this function will move token ahead
	self.compileTerm(level)

        # (op term)*
        while self.tokenizer.symbol() in [ '+', '-', '*', '/', '&', '|', '&lt;', '&gt;', '=' , '&amp;']:

            # op
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            currentOp = self.tokenizer.symbol()

            # term
	    self.compileTerm(level)
            self.fileVm.write( opCommand[ currentOp ] + "\n")

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</expression>" + "\n")

    def compileTerm(self, level):
        Name = ""
        charCounts = 0

        self.file.write( ( ' ' * level * 2) + "<term>" + "\n")
        self.tokenizer.advance()

        # integerConstant | stringConstant | keywordConstant
        if self.tokenizer.tokenType() in [ "integerConstant", "stringConstant" ]:
	    if self.tokenizer.tokenType() ==  "integerConstant":
	        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.intVal() , level)
                self.fileVm.write( "push constant " + self.tokenizer.intVal() + "\n")
	    elif self.tokenizer.tokenType() ==  "stringConstant":
	        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.stringVal() , level)

	        charCounts = len(self.tokenizer.stringVal())

                self.fileVm.write( "push constant " + str(charCounts) + "\n")
                self.fileVm.write( "call String.new 1" + "\n")
                for i in self.tokenizer.stringVal():
                    self.fileVm.write( "push constant " + str( ord(i) ) + "\n")
                    self.fileVm.write( "call String.appendChar 2" + "\n")

	    # keep while loop works fine
	    self.tokenizer.advance()

        # keywordConstant = true | false | null | this
        elif self.tokenizer.keyWord() in [ 'true', 'false', 'null', 'this']:
	    self.writePattern( self.tokenizer.tokenType(), self.tokenizer.keyWord() , level)

            if self.tokenizer.keyWord() == "true":
                self.fileVm.write( "push constant 0" + "\n")
                self.fileVm.write( "not" + "\n")
            elif self.tokenizer.keyWord() == "false":
                self.fileVm.write( "push constant 0" + "\n")
            elif self.tokenizer.keyWord() == "null":
                self.fileVm.write( "push constant 0" + "\n")
            elif self.tokenizer.keyWord() == "this":
                self.fileVm.write( "push pointer 0" + "\n")

	    # keep while loop works fine
	    self.tokenizer.advance()


        # varName | varName '[' expression ']' | subroutineCall
        elif self.tokenizer.tokenType() ==  "identifier" :
	    # varName
	    self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

	    Name = self.tokenizer.identifier()

	    self.tokenizer.advance()
	    # '['
	    if self.tokenizer.symbol() == '[' :
	        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
	        # expression
	        self.compileExpression(level)
	        # ']'
	        self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

                FindTable_And_MemorySegment(self.symbolTables , self.fileVm , self.GetCurrentTableName() , "push", Name )
                self.fileVm.write( "add" + "\n")
                self.fileVm.write( "pop pointer 1" + "\n")
                self.fileVm.write( "push that 0" + "\n")

	        # keep while loop works fine
	        self.tokenizer.advance()
            elif self.tokenizer.symbol() in [ "(", "." ]:

                self.dofunctionName = Name
                # subroutineCall
	        self.tokenizer.backOneToken()
	        self.subroutineCall(level)
	        # keep while loop works fine
	        self.tokenizer.advance()
	    # varName
	    else:
	        FindTable_And_MemorySegment(self.symbolTables , self.fileVm , self.GetCurrentTableName() , "push", Name)

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
	    currentOp = self.tokenizer.symbol()
	    self.compileTerm(level)

            if currentOp == '-':
                self.fileVm.write( "neg" + "\n")
            elif currentOp == '~':
                self.fileVm.write( "not" + "\n")

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</expression>" + "\n")

    def compileExpressionList(self, level):
        self.file.write( ( ' ' * level * 2) + "<expressionList>" + "\n")
        level = level + 1

        self.tokenizer.advance()
        # ( expression ( ','expression )* )?
        if self.tokenizer.symbol() != ")":
            # expression
            self.tokenizer.backOneToken()
            self.compileExpression(level)
            self.dofunctionParameterCount = self.dofunctionParameterCount + 1

            # ( ','expression )*
            while self.tokenizer.symbol() == ',':
                # ','
                self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
                self.compileExpression(level)
                self.dofunctionParameterCount = self.dofunctionParameterCount + 1


        self.fileVm.write( "call " + self.dofunctionName + " " + str(self.dofunctionParameterCount) + "\n")
        self.dofunctionParameterCount = 0

        level = level - 1
        self.file.write( ( ' ' * level * 2) + "</expressionList>" + "\n")

    def subroutineCall(self, level):

        # '(' or '.'
        self.tokenizer.advance()
        if self.tokenizer.symbol() == '(':
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

            #if self.functionType == "method":
            self.fileVm.write( "push pointer 0" + "\n")
            self.dofunctionParameterCount = self.dofunctionParameterCount + 1
            self.dofunctionName = self.currentClassName + '.' + self.dofunctionName
            self.compileExpressionList(level)

            # ')'
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)

        elif self.tokenizer.symbol() == '.':
            # '.'
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            # subroutineName
            self.tokenizer.advance()
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.identifier() , level)

            self.dofunctionName = self.dofunctionName + '.' + self.tokenizer.identifier()

            # '('
            self.tokenizer.advance()
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)
            # ExpressionList
            self.compileExpressionList(level)

            # ')'
            self.writePattern( self.tokenizer.tokenType(), self.tokenizer.symbol() , level)


class SymbolTable():

    def __init__(self, tableName):
        # every element is a tuple, store ( type , kind , #) in dict2
        # use name as key in dict2
        self.tableName = tableName
        self.dict2 = {}
        self.dict1 = { "static":-1, "field":-1, "argument":-1, "local":-1}

    # name(String), type(String), kind( STATIC, FIELD, ARG, VAR)
    def define(self, name, type, kind):
        self.dict2[name] = ( type, kind, self.VarCount(kind) )
        #self.list1.append( (name, type, kind, self.VarCount(kind) ) )


    # kind( STATIC, FIELD, ARG, VAR)
    # Returns int
    # index counts from zero, so the return value is the index you want.
    def VarCount(self, kind):
        self.dict1[kind] = self.dict1[kind] + 1
        return self.dict1[kind]

    def GetVarCount(self, kind):
        return self.dict1[kind]

    def VariableExistOrNot(self, name):
        if name in self.dict2.keys():
            return True
        else:
            return False

    def GetTableName(self):
        return self.tableName

    # name(String)
    # Returns ( STATIC, FIELD, ARG, VAR)
    def KindOf(self, name):
        if name in self.dict2.keys():
            if self.dict2[name][1] == "field":
                return "this"
            else:
                return self.dict2[name][1]
        else:
            return "nothing"

    # name(String)
    # Returns String
    def TypeOf(self, name):
        if name in self.dict2.keys():
            return self.dict2[name][0]
        else:
            return "nothing"

    # name(String)
    # Returns int
    def IndexOf(self, name):
        if name in self.dict2.keys():
            return self.dict2[name][2]
        else:
            return "nothing"

    def PrintAll(self):
        print "Table Name is " + self.tableName
        print "=============================================================== "
        for i in self.dict2.keys():
            print i + "  " + str( self.dict2[i] )
        print "\n"

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
        VmFinalFileName = Orign_file[:-5] + '.vm'
        RemoveFileName = RemoveComments( sys.argv[1] )
        tokens = Tokenize( RemoveFileName , TokenFileName)
        tokenizer = Tokenizer(tokens)
        cplEngine = CompilationEngine(tokenizer, FinalFileName, VmFinalFileName)
        cplEngine.mainEngine()
    elif containJackFile == False :
        JackFilelis = []
        if len(listFilePath) > 1:
            JackFilelist = [ i for i in os.listdir('/'.join(listFilePath[0:-1])) if ".jack" in i]
        else:
            JackFilelist = [ '/' + i for i in os.listdir(sys.argv[1]) if ".jack" in i]
        #print JackFilelist
        for i in JackFilelist:
            Orign_file = sys.argv[1] + i
            TokenFileName = Orign_file[:-5] + 'T.xml'
            FinalFileName = Orign_file[:-5] + '.xml'
            VmFinalFileName = Orign_file[:-5] + '.vm'
            RemoveFileName = RemoveComments( sys.argv[1] + i )
            tokens = Tokenize( RemoveFileName , TokenFileName)
            tokenizer = Tokenizer(tokens)
            cplEngine = CompilationEngine(tokenizer, FinalFileName, VmFinalFileName)
            cplEngine.mainEngine()


