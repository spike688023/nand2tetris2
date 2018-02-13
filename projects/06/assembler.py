import sys,os
import string

aZero= {'0': "101010", '1': "111111", "-1":"111010", "D":"001100", "A":"110000", "!D":"001101", "!A":"110001", "-D":"001111","-A":"110011","D+1":"011111", "A+1":"110111", "D-1":"001110", "A-1":"110010", "D+A":"000010", "D-A":"010011","A-D":"000111","D&A":"000000","A|D":"010101"}

aOne= {'null': "101010", 'M': "110000", '!M': "110001", "-M":"110011", "M+1":"110111", "M-1":"110010", "D+M":"000010", "D-M":"010011", "M-D":"000111","D&M":"000000","D|M":"010101"}

dest= {'null': "000", 'M': "001", "D":"010", "MD":"011", "A":"100", "AM":"101", "AD":"110", "AMD":"111"}
jump= {'null': "000", 'JGT': "001", "JEQ":"010", "JGE":"011", "JLT":"100", "JNE":"101", "JLE":"110", "JMP":"111"}

ST= {'SP': "0", 'LCL': "1", "ARG":"2", "THIS":"3", "THAT":"4", "R0":"0", "R1":"1", "R2":"2", "R3":"3", "R4":"4", "R5":"5", "R6":"6", "R7":"7", "R8":"8", "R9":"9", "R10":"10", "R11":"11", "R12":"12", "R13":"13", "R14":"14", "R15":"15", "SCREEN":"16384", "KBD":"24576"}
#print aZero['0']

# discard comment content
file1 = open(sys.argv[1],'r')
#print file1
lines = file1.read().splitlines()
file1.close()

hackname1 = string.replace(sys.argv[1],".asm",".hack1")
file2 = open(hackname1,'w')
#print hackname1
for i in lines:
    list1 = i.split()
    #print list1
    if len(list1) > 0 and str(list1[0]).find("//") :
        #print list1[0]
        file2.write( list1[0] + "\n")
file2.close()


# process  jump symbol.
# address of ROM starts from 0
hackname2 = string.replace(sys.argv[1],".asm",".hack2")
file1 = open(hackname1,'r')
lines = file1.read().splitlines()
file1.close()
file2 = open(hackname2,'w')
count = string.atoi(str(0))
#print hackname1
for i in lines:
    if i.find(')') > 0:
        ST[i[1:-1]]=count
        #print count
        count -= 1
    else:
        #print "Do i get in"
        file2.write( i + "\n")
    count += 1
file2.close()

# replace all symbol
hackname3 = string.replace(sys.argv[1],".asm",".hack3")
file1 = open(hackname2,'r')
lines = file1.read().splitlines()
file1.close()
file2 = open(hackname3,'w')
count = string.atoi(str(16))
#print hackname1
for i in lines:
    if i.find('@') >= 0 and not i[1:].isdigit():
        if i[1:] not in ST.keys():
            ST[i[1:]]=count
            count += 1
        file2.write( '@' + str(ST[i[1:]]) + "\n")
    else:
        file2.write( i + "\n")
file2.close()

# translate A type instruction
file3 = open(hackname3,'r')
lines2 = file3.read().splitlines()
file3.close()

#print lines2

hackname = hackname1[0:-1]
#print "file4 = " + hackname
file4 = open(hackname,'w')


for i in lines2:
    left = 'null'
    tmp = 'null'
    right = '0'
    third = 'null'

    if i.find('=') >= 0:
        left = i.split('=')[0]
        right= i.split('=')[1]
        tmp = i.split('=')[1]

    if tmp.find(';') >= 0:
        right = tmp.split(';')[0]
        third = tmp.split(';')[1]

    if i.find('=') < 0 and i.find(';') >= 0:
        right = i.split(';')[0]
        third = i.split(';')[1]

    if i.find('@') != -1:
        file4.write( bin( string.atoi(i[1:]) )[2:].zfill(16) + "\n")
    elif right.find('M') >= 0:
        #print i
        file4.write( "1111" + aOne[right] + dest[left] + jump[third] + "\n")
    else:
       #print i
       #print "right = " + right
       #print "left = " + left
       #print "third = " + third
        file4.write( "1110" + aZero[right] + dest[left] + jump[third] + "\n")

file4.close()
os.remove(hackname1)
os.remove(hackname2)
os.remove(hackname3)
