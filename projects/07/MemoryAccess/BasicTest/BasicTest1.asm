//push constant 10
@10
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 0
// Caculate local addresspop local 0
@1
D=M
@0
D=D+A
@255
M=D
@SP
A=M
A=A-1
D=M
@255
A=M
M=D
@SP
M=M-1
