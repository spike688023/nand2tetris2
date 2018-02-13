//push constant 111
@111
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 333
@333
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 888
@888
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop static 8
// Caculate static addresspop static 8
@16
D=M
@8
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
//pop static 3
// Caculate static addresspop static 3
@16
D=M
@3
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
//pop static 1
// Caculate static addresspop static 1
@16
D=M
@1
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
//push static 3
// Caculate static addresspush static 3
@16
D=M
@3
D=D+A
@255
M=D
@255
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push static 1
// Caculate static addresspush static 1
@16
D=M
@1
D=D+A
@255
M=D
@255
A=M
D=M
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
//push static 8
// Caculate static addresspush static 8
@16
D=M
@8
D=D+A
@255
M=D
@255
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
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
