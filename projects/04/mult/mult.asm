// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
// Adds 1+...+100.
	@2 // sum refers to some mem. location.
	M=0 // sum=0

(LOOP)
	@0
	D=M // D=RAM[0]
	@1
	D=D-A // D=i-1
	@0
	M=D  
	@END
	D;JLT // If (i-1)<0 goto END
	@2
	D=M // D=RAM[2]
	@1
	D=D+M // R1=R1+i
	@2
	M=D 
	@LOOP
	0;JMP // Goto LOOP
(END)
	@END
	//0;JMP // Infinite loop
