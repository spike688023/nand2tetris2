//function Sys.init 0
(Sys.init)
//push constant 4000	
@4000
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
@R14
M=D
@SP
A=M
A=A-1
D=M
@R14
A=M
M=D
@SP
M=M-1
//push constant 5000
@5000
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
@R14
M=D
@SP
A=M
A=A-1
D=M
@R14
A=M
M=D
@SP
M=M-1
//call Sys.main 0
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
@0
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
@Sys.main
0;JMP
(RetCount1)
//pop temp 1
// Caculate temp addresspop temp 1
@5
D=A
@1
D=D+A
@R14
M=D
@SP
A=M
A=A-1
D=M
@R14
A=M
M=D
@SP
M=M-1
//label LOOP
(LOOP)
//goto LOOP
@LOOP
0;JMP
//function Sys.main 5
(Sys.main)
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
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 4001
@4001
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
@R14
M=D
@SP
A=M
A=A-1
D=M
@R14
A=M
M=D
@SP
M=M-1
//push constant 5001
@5001
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
@R14
M=D
@SP
A=M
A=A-1
D=M
@R14
A=M
M=D
@SP
M=M-1
//push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 1
// Caculate local addresspop local 1
@1
D=M
@1
D=D+A
@R14
M=D
@SP
A=M
A=A-1
D=M
@R14
A=M
M=D
@SP
M=M-1
//push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 2
// Caculate local addresspop local 2
@1
D=M
@2
D=D+A
@R14
M=D
@SP
A=M
A=A-1
D=M
@R14
A=M
M=D
@SP
M=M-1
//push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 3
// Caculate local addresspop local 3
@1
D=M
@3
D=D+A
@R14
M=D
@SP
A=M
A=A-1
D=M
@R14
A=M
M=D
@SP
M=M-1
//push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
//call Sys.add12 1
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
@Sys.add12
0;JMP
(RetCount2)
//pop temp 0
// Caculate temp addresspop temp 0
@5
D=A
@0
D=D+A
@R14
M=D
@SP
A=M
A=A-1
D=M
@R14
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
//push local 2
// Caculate local addresspush local 2
@1
D=M
@2
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
//push local 3
// Caculate local addresspush local 3
@1
D=M
@3
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
//push local 4
// Caculate local addresspush local 4
@1
D=M
@4
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
//function Sys.add12 0
(Sys.add12)
//push constant 4002
@4002
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
@R14
M=D
@SP
A=M
A=A-1
D=M
@R14
A=M
M=D
@SP
M=M-1
//push constant 5002
@5002
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
@R14
M=D
@SP
A=M
A=A-1
D=M
@R14
A=M
M=D
@SP
M=M-1
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
//push constant 12
@12
D=A
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
