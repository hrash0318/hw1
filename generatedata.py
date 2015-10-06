import random

refFile = "reference3.txt" #Specify i/o files
readsFile = "reads3.txt"

refLength = 1000 #Configurable parameters
readLength = 50
nReads = 600

aligns0 = 0 #Data on output
aligns1 = 0
aligns2 = 0

DNA = dict() #Set up dictionary to convert integers between 0 and 3 to DNA bases
DNA[0] = "G"
DNA[1] = "A"
DNA[2] = "T"
DNA[3] = "C"

ref = "" #Build reference string, random part
randomLength = (3*refLength)/4
for i in range(randomLength):
	ref += DNA[random.randint(0,3)]

for i in range(randomLength, refLength): #Build reference string, copied part
	ref += ref[i-refLength + randomLength]

f = open(refFile,'w') #Write ref to refFile
f.write(ref)
f.close()

reads = [] #Build reads list
tempRead = ''
for i in range(nReads):
	x = random.random()
	if x < .75: #Single-aligns
		aligns1 += 1
		start = random.randint(0,refLength/2) #Pick a random starting point in the first half of the reference (non-copied part)
		for j in range(readLength): #Scan forward through ref to build the read
			tempRead += ref[start + j]
		tempRead += "\n"
		reads.append(tempRead)
		tempRead = ''
	elif x < .85: #Double-aligns
		aligns2 += 1
		start = random.randint(randomLength, refLength-readLength) #Random starting point in the copied portion of the string, far enough from the end that we won't run off the end of ref
		for j in range(readLength):
			tempRead += ref[start + j]
		tempRead += "\n"
		reads.append(tempRead)
		tempRead = ''
	else: #Non-aligns
		aligns0 += 1
		match = 0
		while match != -1: #Iterates until read does not align
			tempRead = ''
			for i in range(readLength):
				tempRead += DNA[random.randint(0,3)]
			match = ref.find(tempRead)
		tempRead += "\n"
		reads.append(tempRead)
		tempRead = ''


f = open(readsFile,'w') #Write reads to readsFile
f.writelines(reads)
f.close()

percentAligns0 = 100*float(aligns0) / float(nReads)
percentAligns1 = 100*float(aligns1) / float(nReads)
percentAligns2 = 100*float(aligns2) / float(nReads)

print("reference length: {}".format(refLength)) #Report summary of results
print("number of reads: {}".format(nReads))
print("read length: {}".format(readLength))
print("percent aligns 0: {:5f}".format(percentAligns0))
print("percent aligns 1: {:5f}".format(percentAligns1))
print("percent aligns 2: {:5f}".format(percentAligns2))