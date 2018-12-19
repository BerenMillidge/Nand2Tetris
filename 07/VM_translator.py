##

# just the smiple code to do the push and pop commands which seem key!

def pop(mem, val):
	# this is the string builder
	s = ""
	s += "// pop " + mem + " " + val + "\n"
	s += "@" + mem + "\n"
	s += "A=M\n"
	s += "D=M\n"
	s += "@" + val + "\n"
	s += "D=D+M\n"
	s += "@SP\n"
	s += "A=M\n"
	s += "M=D\n"
	s += "A=A-1\n"
	s += "D=M\n"
	s += "A=A+1\n"
	s += "A=M\n"
	s += "M=D\n"
	s += "@SP\n"
	s ++ "M=M-1\n"
	return s

def push(mem, val):
	s = ""
	s+= "// push " + mem + " " + val + "\n"
	s += "@" + mem + "\n"
	s += "D=M\n"
	s += "A=M+D\n"
	s += "D=M\n"
	s += "A=D\n" 
	s += "@SP\n"
	s += "A=M\n"
	s += "M=D\n"
	s += "@SP\n"
	s += "M=M+1\n"
	return s

def push2(mem, val): # this one might acctually work
	s = ""
	s+= "// push " + mem + " " + val + "\n"
	s += "@" + mem + "\n"
	s += "A=M\n"
	s += "D=M\n"
	s += "@" + val + "\n"
	s += "D=D+M\n"
	s += "@SP\n"
	s += "A=M\n"
	s +="M=D\n"
	s += "@SP\n"
	s +="M=M+1\n"
	return s

def eq_label(end_label):
	# the assembly at the eq label
	s = ""
	s += "// assembly code for the jump label... sets the answer to 0 and pushes it to stack then jumps to end of instruction"
	s += "D=0\n" # set data to 0
	s += "@SP\n" # goto stack pointer
	s += "A=M\n"
	s += "A=A-1\n" #decrement by 1 to have right address
	s += "M=D\n"
	s += "@" + end_label + "\n" # go to the next instruction # not even sure this is necessary... who knows?
	s += "JMP\n" # jump to this point
	return s

def equals(eq_label):
	s = ""
	s += "// Eq \n"
	s += "@SP\n"
	s += "M=M-1\n" #decrement stack pointer
	s += "A=M\n" # set address to stack pointer variable
	s ++ "D=M\n" # get first val off stack
	s += "A=A-1\n" #  decrement stack again
	s += "D=D-M\n" # substract first and second values of stack
	s += "@" + eq_label + "\n" # prepare jump label
	s += "D;JNE\n" # execute jump if D != 0
	s += "D=1\n" # no jump so succes!
	s += "@SP\n"
	s += "A=M\n"
	s += "A=A-1\n"
	s += "M=D\n"
	return s # this shuold jump sufficiently there so who knows!

def add():
	s = "// add \n"
	s += "@SP\n"
	s += "M=M-1\n"
	s += "A=M\n"
	s += "D=M\n"
	s += "A=A-1\n"
	s += "D=D+M\n"
	s += "M=D\n"
	return s

def sub():
	s = "// sub \n"
	s += "@SP\n"
	s += "M=M-1\n"
	s += "A=M\n"
	s += "D=M\n"
	s += "A=A-1\n"
	s += "D=D-M\n"
	s += "M=D\n"
	return s

def neg():
	s = "// neg \n"
	s += "@SP\n"
	s += "A=M\n"
	s += "A=A-1\n"
	s += "M=-M\n"
	return s
	# you don't need to adjust stack pointer for this which is nice!

def and_asm():
	s = "// and \n"
	s += "@SP\n"
	s += "M=M-1\n"
	s += "A=M\n"
	s += "D=M\n"
	s += "A=A-1\n"
	s += "D=D&M\n"
	s += "M=D\n"
	return s

def or_asm():
	s = "// or \n"
	s += "@SP\n"
	s += "M=M-1\n"
	s += "A=M\n"
	s += "D=M\n"
	s += "A=A-1\n"
	s += "D=D|M\n"
	s += "M=D\n"
	return s

def not_asm():
	s = "// not \n"
	s += "@SP\n"
	s += "A=M\n"
	s += "A=A-1\n"
	s += "M=!M\n"
	return s

def greater_than(gt_label):
	s = ""
	s += "// Eq \n"
	s += "@SP\n"
	s += "M=M-1\n" #decrement stack pointer
	s += "A=M\n" # set address to stack pointer variable
	s ++ "D=M\n" # get first val off stack
	s += "A=A-1\n" #  decrement stack again
	s += "D=D-M\n" # substract first and second values of stack
	s += "@" + gt_label + "\n" # prepare jump label
	s += "D;JGT\n" # execute jump if D != 0
	s += "D=1\n" # no jump so succes!
	s += "@SP\n"
	s += "A=M\n"
	s += "A=A-1\n"
	s += "M=D\n"
	return s

def less_than(lt_label):
	s = ""
	s += "// Eq \n"
	s += "@SP\n"
	s += "M=M-1\n" #decrement stack pointer
	s += "A=M\n" # set address to stack pointer variable
	s ++ "D=M\n" # get first val off stack
	s += "A=A-1\n" #  decrement stack again
	s += "D=D-M\n" # substract first and second values of stack
	s += "@" + lt_label + "\n" # prepare jump label
	s += "D;JLT\n" # execute jump if D != 0
	s += "D=1\n" # no jump so succes!
	s += "@SP\n"
	s += "A=M\n"
	s += "A=A-1\n"
	s += "M=D\n"
	return s

# so these are all the assembly commands I'm going to need... which is nice!.. it's quite a lot , but still doable!