addi $t8,$zero,0 #outer loop iterator to run 5 times
addi $s3,$zero,1 #to check if flag is equal to 1
loopOuter: beq $t8,$t1,loopOuterEnd	#outer loop start
	   addi $s7,$zero,1		#initializing j to be 1
	   addi $s4,$t2,4		#intializing s4 to array[1]
	   loopInner: 	beq $s7,$t1,loopInnerEnd	#outer loop start
	   		addi $t5,$s4,-4			#t5 is location of array[0+j]
	   		#add $t5,$s6,$t2
	   		lw $t4,($t5)			#t4 is value in array[0+j]
	   		addi $t6,$s4,0			#t6 is location of array[1+j]
	   		lw $t7,($t6)			#t7 contains value of array[1+j]
	   		slt $t9,$t4,$t7			#t9 is a flag variable used to compare t4 and t7
	   		
	   		beq $t9,$s3,else
	   		sw $t4,($t6)			#swapping if t4>t7
	   		sw $t7,($t5)
	 
	   else:	addi $s7,$s7,1		#increasing index 
	   		addi $s4,$s4,4
	   		j loopInner
	   loopInnerEnd: addi $t8,$t8,1
	   		 j loopOuter
loopOuterEnd : 

addi $s4,$t2,0			#initializing variables
addi $s3,$t3,0
addi $s7,$zero,0	#i = 0
loop2:  beq $s7,$t1,loop2end		#loop to copy elements from original array t2 to new array t3
	lw $t8,($s4)
	sw $t8,($s3)
      	addi $s7,$s7,1
      	addi $s4,$s4,4
      	addi $s3,$s3,4
        j loop2      
loop2end: