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
//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop that 0              
// Caculate that addresspop that 0              
@4
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
//push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop that 1              
// Caculate that addresspop that 1              
@4
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
//push argument 0
// Caculate argument addresspush argument 0
@2
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
//pop argument 0          
// Caculate argument addresspop argument 0          
@2
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
//label MAIN_LOOP_START
(MAIN_LOOP_START)
//push argument 0
// Caculate argument addresspush argument 0
@2
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
//if-goto COMPUTE_ELEMENT 
@SP
A=M
A=A-1
D=M
@SP
M=M-1
@COMPUTE_ELEMENT
D;JGT
//goto END_PROGRAM        
@END_PROGRAM
0;JMP
//label COMPUTE_ELEMENT
(COMPUTE_ELEMENT)
//push that 0
// Caculate that addresspush that 0
@4
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
//push that 1
// Caculate that addresspush that 1
@4
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
//push constant 1
@1
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
//push argument 0
// Caculate argument addresspush argument 0
@2
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
//pop argument 0          
// Caculate argument addresspop argument 0          
@2
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
//goto MAIN_LOOP_START
@MAIN_LOOP_START
0;JMP
//label END_PROGRAM
(END_PROGRAM)
