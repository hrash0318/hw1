import random
import time

refFile = "reference3.txt" #Specify i/o files
readsFile = "reads3.txt"
alignFile = "alignments3.txt"

aligns0 = 0 #Data on output
aligns1 = 0
aligns2 = 0
runTime = 0.0

ref_file = open(refFile, 'r') #Open i/o files
reads_file = open(readsFile, 'r')
align_file = open(alignFile, 'w')
ref = ref_file.readline() #Copy the reference to a string for easier manipulation

refLength = len(ref) #Gather metadata for later reporting
nReads = sum(1 for _ in reads_file)

startTime = time.time() #Start the timer for alignment

reads_file.seek(0)
for line in reads_file: #Write to alignFile
	read = line.strip()
	align_file.write(read.strip()) #Write out the read we're comparing to the ref
	align_file.write(" {}".format(ref.find(read))) #Write a space, then the first alignment number
	first = ref.find(read)
	if first == -1:
		aligns0 += 1 #Count the number of non-aligning reads
	elif ref[first + 1: refLength].find(read) != -1: #Check for additional alignments
		align_file.write(" {}".format(ref[first+1: refLength].find(read)+first+1)) #Write the second alignment number
		aligns2 += 1 #Count the number of reads with two or more alignments
	else:
		aligns1 += 1 #Count the number of reads with exactly one alignment
	align_file.write("\n")

endTime = time.time() #Stop the timer and compute time ellapsed
runTime = endTime - startTime

ref_file.close() #Close all files
reads_file.close()
align_file.close()

percentAligns0 = 100.0*aligns0 / nReads
percentAligns1 = 100.0*aligns1 / nReads
percentAligns2 = 100.0*aligns2 / nReads
print("reference length: {}".format(refLength))
print("number of reads: {}".format(nReads))
print("aligns 0: {:5f}".format(percentAligns0))
print("aligns 1: {:5f}".format(percentAligns1))
print("aligns 2: {:5f}".format(percentAligns2))
print("elapsed time: {}".format(runTime))