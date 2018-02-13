//function Sys.init 0
(Sys.init)
//push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
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
//label WHILE
(WHILE)
//goto WHILE              
@WHILE
0;JMP
