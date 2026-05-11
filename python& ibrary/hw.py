totalWidth=100
tileWidth=5
tiles=totalWidth//tileWidth
if tiles%2==0:
    tiles=tiles-1
    usedWidth=tiles*tileWidth
    gap=totalWidth-usedWidth
    eachSideGap=gap/2
    
print("number of tile: ",tiles)
print("gab for each side: ",eachSideGap)