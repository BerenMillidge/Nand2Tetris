# okay... attempt to build a simpler assembler for the hack computer in pyhton...
# it's really annoying that this has taken so long and been accompanied by so much procrastintino
# really... it's compeltely disastrous and I'm just useless when down here... I dno't know why...
# and just argh!!!

# ayhow...

import sys
import os
import re
from numpy import binary_repr

# so first case is assembling the requisite dictionaries
def init_command_dict():
	commanddict = {}
	commanddict["0"] = "101010"
	commanddict["1"] = "111111"
	commanddict["-1"] = "111010"
	commanddict["D"] = "001100"
	commanddict["A"] = "110000"
	commanddict["!A"] = "110001"
	commanddict["!D"] = "001101"
	commanddict["-D"] = "001111"
	commanddict["-A"] = "110011"
	commanddict["D+1"] = "011111"
	commanddict["A+1"] = "110111"
	commanddict["D-1"] = "001110"
	commanddict["A-1"] = "110010"
	commanddict["D+A"] = "000010"
	commanddict["D-A"] = "010011"
	commanddict["A-D"] = "000111"
	commanddict["D&A"] = "000000"
	commanddict["D|A"] = "010101"
	commanddict["M"] = "110000"
	commanddict["!M"] = "110001"
	commanddict["-M"] = "110011"
	commanddict["M+1"] = "110111"
	commanddict["M-1"] = "110010"
	commanddict["D+M"] =  "000010"
	commanddict["D-M"] = "010011"
	commanddict["M-D"] = "000111"
	commanddict["D&M"] = "000000"
	commanddict["D|M"] = "010101"
	return commanddict

def init_acommand_dict():
	acommands = {}
	acommands["M"] = "110000"
	acommands["!M"] = "110001"
	acommands["-M"] = "110011"
	acommands["M+1"] = "110111"
	acommands["M-1"] = "110010"
	acommands["D+M"] =  "000010"
	acommands["D-M"] = "010011"
	acommands["M-D"] = "000111"
	acommands["D&M"] = "000000"
	acommands["D|M"] = "010101"
	return acommands

def init_dest_dict():
	dests = {}
	dests["null"] = "000"
	dests["M"] = "001"
	dests["D"] = "010"
	dests["MD"] = "011"
	dests["A"] = "100"
	dests["AM"] = "101"
	dests["AD"] = "110"
	dests["AMD"] = "111"
	return dests

def init_jump_dict():
	jumps = {}
	jumps["null"] = "000"
	jumps["JGT"] = "001"
	jumps["JEQ"] = "010"
	jumps["JGE"] = "011"
	jumps["JLT"] = "100"
	jumps["JNE"]= "101"
	jumps["JLE"] = "110"
	jumps["JMP"] = "111"
	return jumps


def init_symboldict():
	sdict = {}
	sdict["R0"] = 0
	sdict["R1"] = 1
	sdict["R2"] = 2
	sdict["R3"] = 3
	sdict["R4"] = 4
	sdict["R5"] = 5
	sdict["R6"] = 6
	sdict["R7"] = 7
	sdict["R8"] = 8
	sdict["R9"] = 9
	sdict["R10"] = 10
	sdict["R11"] = 11
	sdict["R12"] = 12
	sdict["R13"] = 13
	sdict["R14"] = 14
	sdict["R15"] = 15
	sdict["SCREEN"] ="16384"
	sdict["KBD"] = "24576"
	sdict["SP"] = 0
	sdict["LCL"] = 1
	sdict["ARG"] = 2
	sdict["THIS"] = 3
	sdict["THAT"] = 4
	sdict["LOOP"] = 4
	sdict["STOP"] =18
	sdict["END"] = 22
	return sdict
def to_binary(val):
	return binary_repr(val, width=16)

class Assembler(object):

	def __init__(self, fname,oname):
		self.fname = fname
		self.oname = oname
		# initialize the various dictionaries!
		self.cdict = init_command_dict()
		self.acdict = init_acommand_dict()
		self.ddict = init_dest_dict()
		self.jdict = init_jump_dict()
		self.sdict = init_symboldict()
		# a key question is how to distinbuish between variables and labels... this is relaly furstrating..
		# because if I had done this at 2... the architecture would have been clear in my mind and it wouldn't be a problem
		# argh!
		# should have just done it then!
		#ido'tkowwhattheprolemis withthis... but ugh!
		self.num_symbols = 16 # starts at 16 by the spec

	def write_to_output_file(self,oname, outputs):
		print(outputs)
		with open(oname, 'w+') as f:
			for output in outputs:
				f.write(str(output) + "\n")
		return

	def first_pass(self, lines):
		for line in lines:
			line = line.strip()
			if len(line) > 0:
				if line[0] == "(":
					line[1:-1] = sym
					print("Adding label " + sym)
					self.sdict[sym] = pc +1 # add the new address to the book

			pc += 1


	def assemble(self): # start off with a monster method
		outputs = []
		with open(self.fname, 'r') as f:
			lines = f.readlines()
			out = ""
			pc = 0
			for line in lines:
				out = ""
				line = line.strip()
				print(line)
				if len(line) > 0:
					if line[0] == "/":
						# a comment of some sort... ignore
						pass
					elif line[0] == "" or line[0] == " ":
						# i.e. mpty space... continue
						pass
					# sort out A commands really rapidly without symbols!
					elif line[0] == "@":
						# then an A command!!
						print("A command " + str(line))
						out += "0"

						val = line[1:]
						# check if val is a known symbol or a number
						try:
							val = int(val)
							out += binary_repr(int(val),width=15)
							outputs.append(out) # that is very simple!
						except ValueError:
							# val is a string,which means symbol
							print(val)
							if val in self.sdict.keys():
								v = int(self.sdict[val])
							else:
								v = self.num_symbols + 1
								self.num_symbols +=1
								self.sdict[val] = v
							out += binary_repr(int(v),width=15)
							outputs.append(out)

					elif line[0] == "(":
						# means a label is detected... pass for now
						pass

					elif line[0] in self.ddict.keys() or line[0:1] in self.ddict.keys() or line[0:2] == "AMD" or line[0] in self.cdict.keys() or line[0:1] in self.cdict.keys() or line[0:2] in self.cdict.keys():
						# then definitely a c command... so treat it as such!
						out += "111"
						# first strip out any immediate issues by shrinking line down to size
						if len(line) > 10:
							line = line[0:10]
						if "=" in line and ";" in line:
							dest, cmd = line.split("=")
							dest = dest.strip()
							comp,jmp = cmd.split(";")
							comp = comp.strip()
							jmp = jmp.strip()
						if "=" in line and ";" not in line:
							dest, comp = line.split("=")
							jmp="null"
							dest = dest.strip()
							comp = comp.strip()
						if ";" in line and "=" not in line:
							dest = "null"
							comp, jmp = line.split(";")
							comp = comp.strip()
							jmp = jmp.strip()

						print(dest, comp, jmp)


						# check whether a bit should be set or not!
						if comp in self.acdict.keys():
							out+="1"
						else: 
							out+="0" 
						if comp not in self.cdict.keys():
							print("Command: " + str(comp) + " not found")
							raise
						out += self.cdict[comp]

						if dest not in self.ddict.keys():
							print("Destination Command: " + str(dest) + " not found")
							raise
						out += self.ddict[dest]

						if jmp not in self.jdict.keys():
							print("Jump Command: " + str(jmp) + " not found")
							raise
						out += self.jdict[jmp]

						outputs.append(out)
				pc +=1

		# now just write the ouputs to a file!
		self.write_to_output_file(self.oname, outputs)
		return



if __name__ == '__main__':
	fname = sys.argv[1]
	oname = sys.argv[2]
	a = Assembler(fname, oname)
	a.assemble()
	print(a.sdict)