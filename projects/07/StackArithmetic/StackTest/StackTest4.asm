//push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 3
@3
D=A
@SP
A=M
M=D
@SP
M=M+1
//and
//and
@SP
A=M
A=A-1
D=M
A=A-1
M=M&D
@SP
M=M-1
