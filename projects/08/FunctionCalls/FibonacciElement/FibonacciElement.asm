//goto Sys.init
@Sys.init
0;JMP
//function Main.fibonacci 0
(Main.fibonacci)
//push argument 0
// Caculate argument addresspush argument 0
@2
D=M
@0
D=D+A
@R14
M=D
@R14
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt                     
//lt                     
@SP
A=M
A=A-1
D=M
A=A-1
M=M-D
D=M
@JLT1
D;JLT
@SP
M=M-1
@SP
A=M
A=A-1
M=0
@JGE1
D;JGE
(JLT1)
@SP
M=M-1
@SP
A=M
A=A-1
M=-1
(JGE1)
//if-goto IF_TRUE
@SP
A=M
A=A-1
D=M
@SP
M=M-1
@IF_TRUE
D;JNE
//goto IF_FALSE
@IF_FALSE
0;JMP
//label IF_TRUE          
(IF_TRUE)
//push argument 0        
// Caculate argument addresspush argument 0        
@2
D=M
@0
D=D+A
@R14
M=D
@R14
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//return
//return
// frame = LCLreturn
@1
D=M
@R15
M=D
// retAddr = *(frame-5)return
@5
A=D-A
D=M
@R16
M=D
// *ARG=popreturn
@SP
A=M
A=A-1
D=M
@ARG
A=M
M=D
@SP
M=M-1
// SP=ARG+1return
@ARG
D=M+1
@SP
M=D
// THAT = *(frame-1) return
@1
D=A
@R15
A=M-D
D=M
@4
M=D
// THis = *(frame-2) return
@2
D=A
@R15
A=M-D
D=M
@3
M=D
// ARG= *(frame-3) return
@3
D=A
@R15
A=M-D
D=M
@2
M=D
// LCL = *(frame-4) return
@4
D=A
@R15
A=M-D
D=M
@1
M=D
@R16
A=M
0;JMP
//label IF_FALSE         
(IF_FALSE)
//push argument 0
// Caculate argument addresspush argument 0
@2
D=M
@0
D=D+A
@R14
M=D
@R14
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub
//sub
@SP
A=M
A=A-1
D=M
A=A-1
M=M-D
@SP
M=M-1
//call Main.fibonacci 1  
@RetCount1
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@1
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG
@2
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@3
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@4
D=M
@SP
A=M
M=D
@SP
M=M+1
// SP - nArgs - 5
@1
D=A
@SP
D=M-D
@R16
M=D
@5
D=A
@R16
M=M-D
D=M
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto function
@Main.fibonacci
0;JMP
(RetCount1)
//push argument 0
// Caculate argument addresspush argument 0
@2
D=M
@0
D=D+A
@R14
M=D
@R14
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub
//sub
@SP
A=M
A=A-1
D=M
A=A-1
M=M-D
@SP
M=M-1
//call Main.fibonacci 1  
@RetCount2
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@1
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG
@2
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@3
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@4
D=M
@SP
A=M
M=D
@SP
M=M+1
// SP - nArgs - 5
@1
D=A
@SP
D=M-D
@R16
M=D
@5
D=A
@R16
M=M-D
D=M
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto function
@Main.fibonacci
0;JMP
(RetCount2)
//add                    
//add                    
@SP
A=M
A=A-1
D=M
A=A-1
M=M+D
@SP
M=M-1
//return
//return
// frame = LCLreturn
@1
D=M
@R15
M=D
// retAddr = *(frame-5)return
@5
A=D-A
D=M
@R16
M=D
// *ARG=popreturn
@SP
A=M
A=A-1
D=M
@ARG
A=M
M=D
@SP
M=M-1
// SP=ARG+1return
@ARG
D=M+1
@SP
M=D
// THAT = *(frame-1) return
@1
D=A
@R15
A=M-D
D=M
@4
M=D
// THis = *(frame-2) return
@2
D=A
@R15
A=M-D
D=M
@3
M=D
// ARG= *(frame-3) return
@3
D=A
@R15
A=M-D
D=M
@2
M=D
// LCL = *(frame-4) return
@4
D=A
@R15
A=M-D
D=M
@1
M=D
@R16
A=M
0;JMP
//function Sys.init 0
(Sys.init)
@261
D=A
@0
M=D
//push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
//call Main.fibonacci 1   
@RetCount3
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@1
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG
@2
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@3
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@4
D=M
@SP
A=M
M=D
@SP
M=M+1
// SP - nArgs - 5
@1
D=A
@SP
D=M-D
@R16
M=D
@5
D=A
@R16
M=M-D
D=M
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto function
@Main.fibonacci
0;JMP
(RetCount3)
//label WHILE
(WHILE)
//goto WHILE              
@WHILE
0;JMP
