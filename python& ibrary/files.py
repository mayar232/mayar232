infile=open("C:/Users/DELL/Desktop/data.txt","r")
line1=infile.readline()
print(line1)
line2=infile.readline()
print(line1)
infile.close()
print("----------------")
############################


infile=open("C:/Users/DELL/Desktop/data.txt","r")
line=infile.readline()
nolines=1
while line!="":
    print(line)
    nolines+=1
    line=infile.readline()
infile.close()
print("----------------")
#####################
infile=open("C:/Users/DELL/Desktop/data.txt","r")
lines=infile.readlines()
print(lines)
for line in range(len( lines)):
      lines[line] = int(lines[line].strip())#add strip to remove/n"
print(sum(lines)/len(lines))
infile.close()
###################
infile=open("C:/Users/DELL/Desktop/data.txt","r")
lines= infile.read().split("\n")

print(lines) 
