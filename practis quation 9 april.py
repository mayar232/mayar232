def calculation(a, b):
    summ = a + b
    sub = a - b
    return summ, sub

res = calculation(40, 10)
print(res)

def show_employee(name,salary=8000):
    print("name:",name,"salary:",salary)
show_employee("ben",500)
show_employee("jesica")

##############
def outer(a,b):
    def inner():
        return a+b
    return inner()+ 5
print(outer(10,10))
def factoril(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
    
###############
def summ(n):
    if n == 0:
        return 0
    return n+summ(n-1)

print(summ(10))
    
############## 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
           

###########
def summ(n):
    if n == 0:
        return 0
    return n+summ(n-1)

print(summ(10))
#use recursive
def digit(n):
    if n == 0:
        return n
    return 1+digit(n//10)
print(digit(175))              
