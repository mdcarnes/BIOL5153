#! /usr/bin/env python3

#read in the genome in fasta format and store it in a variable, use SeqIO for this.
WatermelonSequence = open("watermelon.fsa")
WatermelonSequenceContents = WatermelonSequence.read()
#print(WatermelonSequenceContents)


#Open the GFF file
#
with open("watermelon.gff") as f:
#generate a list
	data = []
#read the list in line by line
	for line in f:
#make each column a list element using tab characters to split,
#keep only columns 3 and 4, the start and stop coords

		data_line = line.rstrip().split('\t')[3:5:]
#generate a growing list of each of the lists being generated
		data.append(data_line)
#print to screen

print (data)
