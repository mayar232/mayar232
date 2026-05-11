a="GeeksForGeeks"
upper=lambda x:x.upper()
print(upper(a))

area=lambda x,y:x*y
print("-------")

check=lambda x:"posetive"if x > 0 else "negative" if x<0 else"Zero"
print(check(5))
print(check(-2))
print(check(0))

 
def func1(*args):
    for arf in args:
        print(10,20,3)
func1(10,20)
func1("hello",3,14,True)
func1(1,2,3,4)
func1()


