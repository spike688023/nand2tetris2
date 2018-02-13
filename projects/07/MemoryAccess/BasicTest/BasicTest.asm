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
//push constant 21
@21
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 22
@22
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop argument 2
// Caculate argument addresspop argument 2
@2
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
//pop argument 1
// Caculate argument addresspop argument 1
@2
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
//push constant 36
@36
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop this 6
// Caculate this addresspop this 6
@3
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
//push constant 42
@42
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 45
@45
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop that 5
// Caculate that addresspop that 5
@4
D=M
@5
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
//pop that 2
// Caculate that addresspop that 2
@4
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
//push constant 510
@510
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop temp 6
// Caculate temp addresspop temp 6
@5
D=M
@6
D=D+A
@5
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
//push local 0
// Caculate local addresspush local 0
@1
D=M
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
//push that 5
// Caculate that addresspush that 5
@4
D=M
@5
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
//push argument 1
// Caculate argument addresspush argument 1
@2
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
//push this 6
// Caculate this addresspush this 6
@3
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
//push this 6
// Caculate this addresspush this 6
@3
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
//push temp 6
// Caculate temp addresspush temp 6
@5
D=M
@6
D=D+A
@5
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
