
try:
    infile=open("C:/Users/DELL/Desktop/math.txt","r")
    line=infile.readline()
    print(line)
    print(5/0)

except IOError:
    print("could not open input file")
except Exception as exceptobj:
    print("Error:",str(exceptobj))
    
    
inputOK=False
while(inputOK==False):
    try:
        num= input("entrer a number: ")
        num=float(num)
        inputOK=True
    except ValueError:
        print("non nomric try again"% num)
        
num=num*2
print(num)