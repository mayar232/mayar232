#1 Write a function table(n) that prints multiplication table of a number.
def table(n):
     for num in range (1,13):
         
         print(n,"X",num,"=",num*n)
         
table(5)
print()

    
#2Write a function reverse_word(word) that returns the reversed word.
def reverse_word(word):
      reverse=""
      for i in range(len(word)-1,-1,-1):
           reverse= reverse+word[i]
      return  reverse
print (reverse_word("mayar" ))
print()
# 3Write a function factorial(n) that returns factorial of a number.
def factorial(n):
    total=1
    for i in range(1,n+1):
        
        total=total*i
    print(total)

factorial(3)

print()

        

 #4write a function Fibonacci Number
def Fibonacci(n):    
    a=0
    b=1
    print(a)
    for i in range(n):
        temp=a
        a=b
        b=b+temp
        if a>7:
            break
        else:
            print(a)
Fibonacci(5)       
           
        
            
#5 Write a function sum_squares(n) that returns 1^1 + ... + n^n .
def sum_squares(n):
    summ=0
    for i in range (1,n+1):
        result=i**i
        summ+=result
    return summ
print(sum_squares(4))
        
         
     

    