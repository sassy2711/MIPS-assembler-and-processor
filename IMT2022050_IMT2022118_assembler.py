import re

instructions = ["addi $t8,$zero,0", 	#instructions stores each instruction in the solution.asm as a string, this is hardcoded(done manually)
"addi $s3,$zero,1", 
"loopOuter: beq $t8,$t1,loopOuterEnd",
	   "addi $s7,$zero,1",
	   "addi $s4,$t2,4",
		"loopInner: beq $s7,$t1,loopInnerEnd",
	   		"addi $t5,$s4,-4",
	   		"lw $t4,($t5)",
	   		"addi $t6,$s4,0",
	   		"lw $t7,($t6)",
	   		"slt $t9,$t4,$t7",
	   		"beq $t9,$s3,else",
	   		"sw $t4,($t6)",
	   		"sw $t7,($t5)",
	 "else:	addi $s7,$s7,1",
	   		"addi $s4,$s4,4",
	   		"j loopInner",
	   "loopInnerEnd: addi $t8,$t8,1",
	   		 "j loopOuter",
"loopOuterEnd:",
"addi $s4,$t2,0",
"addi $s3,$t3,0",
"addi $s7,$zero,0",
"loop2:	beq $s7,$t1,loop2end",
	"lw $t8,($s4)",
	"sw $t8,($s3)",
	  	"addi $s7,$s7,1",
	  	"addi $s4,$s4,4",
	  	"addi $s3,$s3,4",
		"j loop2",  
"loop2end:"]

#these dictionaries store the binary values of the various things in the instructions

#reg_dict stores 5 bit binary values for registers
reg_dict = {"'$s3'": "10011", "'$s4'" : "10100", "'$s7'": "10111", "'$t1'": "01001", "'$t2'" : "01010", "'$t3'" : "01011", "'$t4'" : "01100", "'$t5'" : "01101", "'$t6'" : "01110", "'$t7'" : "01111", "'$t8'" : "11000", "'$t9'" : "11001", "'$zero'" : "00000"}
#opcode_dict stores 6 bit binary values for the functions
opcode_dict = {"'addi'" : "001000", "'beq'" : "000100", "'lw'" : "100011", "'sw'" : "101011", "'slt'" : "000000", "'j'" : "000010"}
#immediate_dict stores 16 bit binary values for all immediate values used in the program
immediate_dict = {"'loopOuterEnd'" : "0000000000010000", "'loopInnerEnd'" : "0000000000001011", "'loop2end'" : "0000000000001100", "'else'" : "0000000000000010", "'0'" : "0000000000000000", "'1'" : "0000000000000001", "'4'" : "0000000000000100", "'-4'" : "1111111111111100"}
#funct_dict stores 6 bit binary values for the funct field in R type instructions
funct_dict = {"'slt'" : "101010"}
#address_dict stores 32 bit binary values of the addresses of jump instructions
address_dict = {"'loopInner'" : "00000000010000000000000010001000", "'loopOuter'" : "00000000010000000000000001010100", "'loop2'" : "00000000010000000000000010100100"}

word_list = []	#this will contain lists of each word of an instruction(wont include commas and spaces)(word_list[i] = ith instruction as a list with its elements as word strings)
for i in instructions:
	temp_list = re.split('\t|,| ', i)
	word_list.append(temp_list)

machine_code = []	#this will contain binary output of each instruction(machine_code[i] = binary encoding of the ith instruction)

for i in word_list:	#iterating through the instructions
	instruction = i
	#if the first word of the instruction is a procedure name, we pop it because it does not play any role in the binary encoding of the instruction
	if instruction[0] == "loopOuter:" or instruction[0]	 == "loopOuterEnd:" or instruction[0] == "loopInner:" or instruction[0] == "loopInnerEnd:" or instruction[0] == "else:" or instruction[0] == "loop2:" or instruction[0] == "loop2end:":
		instruction.pop(0)
	if instruction: #checking if the instruction is not empty
		#Now we just check which instruction it is and assign the binary values from the dictionaries
		if instruction[0] == "beq":	
			opcode = opcode_dict[f"'{(instruction[0])}'"]
			rs = reg_dict[f"'{(instruction[1])}'"]
			rt = reg_dict[f"'{(instruction[2])}'"]
			imm = immediate_dict[f"'{(instruction[3])}'"]
			machine_str = opcode+rs+rt+imm
			machine_code.append(machine_str)
		if instruction[0] == "lw" or instruction[0] == "sw":
			opcode = opcode_dict[f"'{(instruction[0])}'"]
			rt = reg_dict[f"'{(instruction[1])}'"]
			rs = reg_dict[f"'{(instruction[2][1:4])}'"]
			imm = immediate_dict["'0'"]
			machine_str = opcode+rs+rt+imm
			machine_code.append(machine_str)
		if instruction[0] == "addi":
			opcode = opcode_dict[f"'{(instruction[0])}'"]
			rt = reg_dict[f"'{(instruction[1])}'"]
			rs = reg_dict[f"'{(instruction[2])}'"]
			imm = immediate_dict[f"'{(instruction[3])}'"]
			machine_str = opcode+rs+rt+imm
			machine_code.append(machine_str)
		if instruction[0] == "slt":
			opcode = opcode_dict[f"'{(instruction[0])}'"]
			rd = reg_dict[f"'{(instruction[1])}'"]
			rs = reg_dict[f"'{(instruction[2])}'"]
			rt = reg_dict[f"'{(instruction[3])}'"]
			funct = funct_dict[f"'{(instruction[0])}'"]
			shamt = "00000"
			machine_str = opcode+rs+rt+rd+shamt+funct
			machine_code.append(machine_str)
		if instruction[0] == "j":
			opcode = opcode_dict[f"'{(instruction[0])}'"]
			address = address_dict[f"'{(instruction[1])}'"]
			shortened_address = address[4:30]
			machine_str = opcode+shortened_address
			machine_code.append(machine_str)
		
for i in machine_code: #printing the machine code line by line
	print(i)