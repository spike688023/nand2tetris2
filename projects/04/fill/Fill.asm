// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
	@3
	M=-1

(LOOP)
	@16384
	D=A
	@2
	M=D
	@24576
	D=M
	@LOOPBLACK
	D;JNE // If (i!=0)0 goto LOOPBLACK
(LOOPWHITE)
	@0
        D=A
	@2
        A=M
	M=D  // RAM[address] = 0
	@2
        D=M+1
        M=D
	@24575
        D=A-D
	@LOOPWHITE
	D;JGE // Goto LOOPWHITE
	@LOOP
	0;JMP // Infinite loop

(LOOPBLACK)
	@3
        D=M
	@2
        A=M  // A=16384
        M=D  // RAM[16384] = -1
	@2
        D=M+1
        M=D
	@24575
        D=A-D
	@LOOPBLACK
	D;JGE // Goto LOOPBALCK
	@LOOP
	0;JMP // Infinite loop
