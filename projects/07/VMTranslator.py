import sys,os
import string

aZero= {'0': "101010", '1': "111111", "-1":"111010", "D":"001100", "A":"110000", "!D":"001101", "!A":"110001", "-D":"001111","-A":"110011","D+1":"011111", "A+1":"110111", "D-1":"001110", "A-1":"110010", "D+A":"000010", "D-A":"010011","A-D":"000111","D&A":"000000","A|D":"010101"}

aOne= {'null': "101010", 'M': "110000", '!M': "110001", "-M":"110011", "M+1":"110111", "M-1":"110010", "D+M":"000010", "D-M":"010011", "M-D":"000111","D&M":"000000","D|M":"010101"}

dest= {'null': "000", 'M': "001", "D":"010", "MD":"011", "A":"100", "AM":"101", "AD":"110", "AMD":"111"}
jump= {'null': "000", 'JGT': "001", "JEQ":"010", "JGE":"011", "JLT":"100", "JNE":"101", "JLE":"110", "JMP":"111"}

ST= {'SP': "0", 'LCL': "1", "ARG":"2", "this":"3", "that":"4", "R0":"0", "R1":"1", "R2":"2", "R3":"3", "R4":"4", "R5":"5", "R6":"6", "R7":"7", "R8":"8", "R9":"9", "R10":"10", "R11":"11", "R12":"12", "R13":"13", "R14":"14", "R15":"15", "SCREEN":"16384", "KBD":"24576", "temp":'5','static':'16','pointer':'3'}
count= {'eq': 0, 'neq': 0, "lt":0, "gt":0, "le":0, "ge":0}
#print aZero['0']

def main():
    # discard comment content
    file1 = open(sys.argv[1],'r')
    #print file1
    lines = file1.read().splitlines()
    file1.close()

    asm1 = string.replace(sys.argv[1],".vm",".asm1")
    file2 = open(asm1,'w')
    #print hackname1
    for i in lines:
        list1 = i.split()
        #print list1
        if len(list1) > 0 and i.find("//") < 0:
            #print list1[0]
            file2.write( i + "\n")
    file2.close()

    file3 = open(asm1,'r')
    lines2 = file3.read().splitlines()
    file3.close()

    asm = asm1[0:-1]
    #print "file4 = " + hackname
    file4 = open(asm,'w')

    for i in lines2:
        list1 = i.split()

        file4.write( '//' + i + "\n")
        if len(list1) == 3:
            if list1[1] == "constant":
                file4.write( '@' + list1[2] + "\n")
                file4.write( 'D=A'  + "\n")
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'M=D'  + "\n")
            elif list1[1] == 'static':
                file4.write( '// Caculate static address' + i + "\n")
                file4.write( '@' + ST['static'] + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( '@' + list1[2] + "\n")
                file4.write( 'D=D+A'  + "\n")
                file4.write( '@255' + "\n")
                file4.write( 'M=D'  + "\n")
            elif list1[1] == 'local':
                file4.write( '// Caculate local address' + i + "\n")
                file4.write( '@' + ST['LCL'] + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( '@' + list1[2] + "\n")
                file4.write( 'D=D+A'  + "\n")
                file4.write( '@255' + "\n")
                file4.write( 'M=D'  + "\n")
            elif list1[1] == 'argument':
                file4.write( '// Caculate argument address' + i + "\n")
                file4.write( '@' + ST['ARG'] + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( '@' + list1[2] + "\n")
                file4.write( 'D=D+A'  + "\n")
                file4.write( '@255' + "\n")
                file4.write( 'M=D'  + "\n")
            elif list1[1] == 'this':
                file4.write( '// Caculate this address' + i + "\n")
                file4.write( '@' + ST['this'] + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( '@' + list1[2] + "\n")
                file4.write( 'D=D+A'  + "\n")
                file4.write( '@255' + "\n")
                file4.write( 'M=D'  + "\n")
            elif list1[1] == 'that':
                file4.write( '// Caculate that address' + i + "\n")
                file4.write( '@' + ST['that'] + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( '@' + list1[2] + "\n")
                file4.write( 'D=D+A'  + "\n")
                file4.write( '@255' + "\n")
                file4.write( 'M=D'  + "\n")
            elif list1[1] == 'pointer':
                file4.write( '// Caculate pointer address' + i + "\n")
                file4.write( '@' + ST['pointer'] + "\n")
                file4.write( 'D=A'  + "\n")
                file4.write( '@' + list1[2] + "\n")
                file4.write( 'D=D+A'  + "\n")
                file4.write( '@255' + "\n")
                file4.write( 'M=D'  + "\n")
            elif list1[1] == 'temp':
                file4.write( '// Caculate temp address' + i + "\n")
                file4.write( '@' + ST['temp'] + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( '@' + list1[2] + "\n")
                file4.write( 'D=D+A'  + "\n")
                file4.write( '@5' "\n")
                file4.write( 'D=D+A'  + "\n")
                file4.write( '@255' + "\n")
                file4.write( 'M=D'  + "\n")

            if list1[0] == 'push':
                if list1[1] != 'constant':
                    file4.write( '@255' + "\n")
                    file4.write( 'A=M'  + "\n")
                    file4.write( 'D=M'  + "\n")
                    file4.write( '@SP'  + "\n")
                    file4.write( 'A=M'  + "\n")
                    file4.write( 'M=D'  + "\n")
                file4.write( '@SP'  + "\n")
                file4.write( 'M=M+1'  + "\n")
            elif list1[0] == 'pop':
                if list1[1] != 'constant':
                    file4.write( '@SP'  + "\n")
                    file4.write( 'A=M'  + "\n")
                    file4.write( 'A=A-1'  + "\n")
                    file4.write( 'D=M'  + "\n")
                    file4.write( '@255' + "\n")
                    file4.write( 'A=M'  + "\n")
                    file4.write( 'M=D'  + "\n")
                file4.write( '@SP'  + "\n")
                file4.write( 'M=M-1'  + "\n")


        elif len(list1) == 1:
            file4.write( '//' + i + "\n")
            if list1[0] == 'add':
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'M=M+D'  + "\n")
                file4.write( '@SP'  + "\n")
                file4.write( 'M=M-1'  + "\n")
            elif list1[0] == 'sub':
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'M=M-D'  + "\n")
                file4.write( '@SP'  + "\n")
                file4.write( 'M=M-1'  + "\n")
            elif list1[0] == 'eq':
                count['eq'] = count['eq'] + 1
                count['neq'] = count['neq'] + 1
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'M=M-D'  + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( '@JEQ' + str(count['eq']) + "\n")
                file4.write( 'D;JEQ'  + "\n")
                # a - b != 0
                file4.write( '@SP'  + "\n")
                file4.write( 'M=M-1'  + "\n")
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'M=0'  + "\n")
                file4.write( '@JNE' + str(count['neq']) + "\n")
                file4.write( 'D;JNE'  + "\n")
                file4.write( '(JEQ' + str(count['eq']) + ')' + "\n")
                # a - b  == 0
                file4.write( '@SP'  + "\n")
                file4.write( 'M=M-1'  + "\n")
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'M=-1'  + "\n")
                file4.write( '(JNE' + str(count['neq']) + ')' + "\n")
            elif list1[0] == 'neg':
                count['gt'] = count['gt'] + 1
                count['lt'] = count['lt'] + 1
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( '@JGT' + str(count['gt']) + "\n")
                file4.write( 'D;JGT' + "\n")
                # a < b
                file4.write( 'D=!D'  + "\n")
                file4.write( 'D=D+1'  + "\n")
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'M=D'  + "\n")
                file4.write( '@JLT' + str(count['lt']) + "\n")
                file4.write( '0;JMP'  + "\n")
                file4.write( '(JGT' + str(count['gt']) + ')' + "\n")
                # a > b
                file4.write( 'D=!D'  + "\n")
                file4.write( 'D=D+1'  + "\n")
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'M=D'  + "\n")
                file4.write( '(JLT' + str(count['lt']) + ')' + "\n")
            elif list1[0] == 'gt':
                count['gt'] = count['gt'] + 1
                count['le'] = count['le'] + 1
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'M=M-D'  + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( '@JGT' + str(count['gt']) + "\n")
                file4.write( 'D;JGT'  + "\n")
                # a <= b
                file4.write( '@SP'  + "\n")
                file4.write( 'M=M-1'  + "\n")
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'M=0'  + "\n")
                file4.write( '@JLE' + str(count['le']) + "\n")
                file4.write( 'D;JLE'  + "\n")
                file4.write( '(JGT' + str(count['gt']) + ')' + "\n")
                # a > b
                file4.write( '@SP'  + "\n")
                file4.write( 'M=M-1'  + "\n")
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'M=-1'  + "\n")
                file4.write( '(JLE' + str(count['le']) + ')' + "\n")
            elif list1[0] == 'lt':
                count['lt'] = count['lt'] + 1
                count['ge'] = count['ge'] + 1
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'M=M-D'  + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( '@JLT' + str(count['lt']) + "\n")
                file4.write( 'D;JLT'  + "\n")
                # a >= b
                file4.write( '@SP'  + "\n")
                file4.write( 'M=M-1'  + "\n")
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'M=0'  + "\n")
                file4.write( '@JGE' + str(count['ge']) + "\n")
                file4.write( 'D;JGE'  + "\n")
                file4.write( '(JLT' + str(count['lt']) + ')' + "\n")
                # a < b
                file4.write( '@SP'  + "\n")
                file4.write( 'M=M-1'  + "\n")
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'M=-1'  + "\n")
                file4.write( '(JGE' + str(count['ge']) + ')' + "\n")
            elif list1[0] == 'and':
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'M=M&D'  + "\n")
                file4.write( '@SP'  + "\n")
                file4.write( 'M=M-1'  + "\n")
            elif list1[0] == 'or':
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'M=M|D'  + "\n")
                file4.write( '@SP'  + "\n")
                file4.write( 'M=M-1'  + "\n")
            elif list1[0] == 'not':
                file4.write( '@SP'  + "\n")
                file4.write( 'A=M'  + "\n")
                file4.write( 'A=A-1'  + "\n")
                file4.write( 'D=M'  + "\n")
                file4.write( 'M=!D'  + "\n")

    file4.close()
    os.remove(asm1)
if  __name__ =='__main__':
    main()
