#cube 
sideLength=2
def cuBeVolume(sideLength):
  if sideLength>=0:
        return sideLength**3
  else:
        return(0)
print(cuBeVolume(-3))

print()

# pyramid 
def pyramidvolume ( basearea,highe):
    
    volume=(1/3)*(highe*basearea)
  
    return volume
 
print(pyramidvolume (3,5))
print()


# prime def
def isprime(num):
 
    if num<=1:
        return
    i=2
    while i<num:
        if num%i==0:
          return False
        i+=1
    return True
print(isprime(4))

print()