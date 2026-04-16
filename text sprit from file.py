infile=open("C:/Users/DELL/Desktop/math.txt","r")
text=infile.read()
wordList=text.split()
print("the word: ",wordList)
print("the number of words:",len(wordList))
for i in range(len(wordList)):
      wordList[i]= wordList[i].lower().strip()
theCount=wordList.count("the")
print(theCount)
#way 2:
rep=0
for i in range(len(wordList)):
    if wordList[i].lower().strip()=="the":
        rep=rep+1
print(rep)
# calculat index:
listTheIndex=[]
for i in range(len(wordList)):
    if wordList[i]=="the":
            listTheIndex.append(i)
for index in range (len(listTheIndex)):
        if index==len(listTheIndex)-1:
            print(wordList[listTheIndex[index]:])
        else:
         print(wordList[listTheIndex[index]:listTheIndex[index+1]])


    infile.close()

