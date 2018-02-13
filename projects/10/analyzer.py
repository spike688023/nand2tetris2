import sys,os
import string,shutil
import tokenizer

keywordTable = { "class":"<keyword> class </keyword>", "constructor":"<keyword> constructor </keyword>", "function":"<keyword> function </keyword>", "method":"<keyword> method </keyword>", "field":"<keyword> field </keyword>", "static":"<keyword> static </keyword>", "var":"<keyword> var </keyword>", "int":"<keyword> int </keyword>","char":"<keyword> char </keyword>","boolean":"<keyword> boolean </keyword>","void":"<keyword> void </keyword>","true":"<keyword> true </keyword>","false":"<keyword> fasle </keyword>","null":"<keyword> null </keyword>","this":"<keyword> this </keyword>", "let":"<keyword> let </keyword>", "do":"<keyword> do </keyword>", "if":"<keyword> if </keyword>",  "while":"<keyword> while </keyword>", "return":"<keyword> return </keyword>" }

symbolTable = { "{":"<symbol> { </symbol>", "}":"<symbol> } </symbol>", "(":"<symbol> ( </symbol>", ")":"<symbol> ) </symbol>", "[":"<symbol> [ </symbol>", "]":"<symbol> ] </symbol>", ".":"<symbol> . </symbol>", ",":"<symbol> : </symbol>" , ";":"<symbol> ; </symbol>", "+":"<symbol> + </symbol>" , "-":"<symbol> - </symbol>" ,"*":"<symbol> * </symbol>" ,"/":"<symbol> / </symbol>" ,"&":"<symbol> & </symbol>" , "|":"<symbol> | </symbol>", "<":"<symbol> &lt </symbol>", ">":"<symbol> &gt </symbol>", "=":"<symbol> = </symbol>",  "~":"<symbol> &amp </symbol>"}

def RemoveComments( OriginFile ):
    RemoveComments = Orign_file[:-5] + 'RemoveComments.xml'
    writtenFile = open(RemoveComments,'w')
    jackfile = open( OriginFile,'r' )
    # delete comments
    lines = jackfile.read().splitlines()
    for i in lines:
        list1 = i.split()
        onlycomments = False
        if "//" in list1[0]: onlycomments = True
        index = i.find("//")
        index2 = i.find("/**")
        if len(list1) > 0 and index < 0 and index2 < 0:
            writtenFile.write( i + "\n")
        elif len(list1) > 0 and index > 0 and onlycomments == false:
            writtenFile.write( i[0:index] + "\n")
    writtenFile.close()
    jackfile.close()
    return RemoveComments

def Tokenize( RemoveCommentsFile, TokenFileName):
    pass


if  __name__ =='__main__':
    listFilePath = sys.argv[1].split('/')
    containJackFile = True
    if ".jack" not in sys.argv[1]:
        containJackFile = False

    RemoveCommentsFile = ''
    if containJackFile == True:
        Orign_file= sys.argv[1]
        TokenFileName = Orign_file[:-5] + 'T.xml'
        FinalFileName = Orign_file[:-5] + '.xml'
        RemoveFileName = RemoveComments( sys.argv[1] )
        #print RemoveFileName
        RemoveCommentsFile = open(RemoveFileName,'r')
        Tokenize( RemoveCommentsFile , TokenFileName)

