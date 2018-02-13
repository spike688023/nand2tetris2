//push constant 0
@0
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
//label LOOP_START
(LOOP_START)
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
//if-goto LOOP_START  
@SP
A=M
A=A-1
D=M
@SP
M=M-1
@LOOP_START
D;JGT
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
