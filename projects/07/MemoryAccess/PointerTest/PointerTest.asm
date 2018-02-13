//push constant 3030
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 0
// Caculate pointer addresspop pointer 0
@3
D=A
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
//push constant 3040
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 1
// Caculate pointer addresspop pointer 1
@3
D=A
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
//push constant 32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop this 2
// Caculate this addresspop this 2
@3
D=M
@2
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
//push constant 46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop that 6
// Caculate that addresspop that 6
@4
D=M
@6
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
//push pointer 0
// Caculate pointer addresspush pointer 0
@3
D=A
@0
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
//push pointer 1
// Caculate pointer addresspush pointer 1
@3
D=A
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
//push this 2
// Caculate this addresspush this 2
@3
D=M
@2
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
//push that 6
// Caculate that addresspush that 6
@4
D=M
@6
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
