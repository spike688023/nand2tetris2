//function SimpleFunction.test 2
(SimpleFunction.test)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push local 0
// Caculate local addresspush local 0
@1
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
//push local 1
// Caculate local addresspush local 1
@1
D=M
@1
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
//not
//not
@SP
A=M
A=A-1
D=M
M=!D
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
