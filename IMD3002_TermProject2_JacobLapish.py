import maya.cmds as cmds
import random

streetGet = None
heightGet = None
densGet = None
blockGet = None
countGet = None
randomCheck = False

UI = cmds.window(title = "City Maker", width=400)

cmds.columnLayout(rowSpacing=10)

cmds.text(label="City Maker")
#commandOff()
#commandOn()
cmds.text(label="City Attributes")
cmds.text(label="Street size (max 4)")
street = cmds.intField( minValue=1, maxValue=4, value=1, cc='setStreet()')
cmds.text(label="Building Height (max 10)")
bHeight = cmds.intField( minValue=1, maxValue=10, value=1, cc='setHeight()')
cmds.text(label="Building Density (max 10)")
bDens = cmds.intField( minValue=1, maxValue=10, value=1, cc='setDens()')
cmds.text(label="Block Size (max 10)")
block = cmds.intField( minValue=1, maxValue=10, value=1, cc='setBlock()')
cmds.text(label="Block Count (max 9)")
count = cmds.intField( minValue=1, maxValue=9, value=1, cc='setCount()')
cmds.checkBox( label='Randomize', onc='randomCheck=True', ofc='randomCheck=False')

cmds.button(label="Make City", command="makeCity()")


cmds.showWindow(UI)

#SETUP SETUP SETUP SETUP SETUP SETUP SETUP SETUP SETUP SETUP SETUP
def setStreet():
    streetInt = cmds.intField(street, q=1, v=1)
    print(streetInt)
    streetGet = streetInt
    return streetInt

def setHeight():
    heightInt = cmds.intField(bHeight, q=1, v=1)
    print(heightInt)
    heightGet = heightInt
    return heightInt

def setDens():
    densInt = cmds.intField(bDens, q=1, v=1)
    print(densInt)
    densGet = densInt
    return densInt

def setBlock():
    blockInt = cmds.intField(block, q=1, v=1)
    print(blockInt)
    blockGet = blockInt
    return blockInt  

def setCount():
    countInt = cmds.intField(count, q=1, v=1)
    print(countInt)
    countGet = countInt
    return countInt  
    
def makeCity():
    if(randomCheck == False):
        streetGet = setStreet()
        heightGet = setHeight()
        densGet = setDens()
        blockGet = setBlock()
        countGet = setCount()
        generateCity(streetGet, heightGet, densGet, blockGet, countGet)
    elif(randomCheck == True):
        streetGet = random.randint(1, 4)
        heightGet = random.randint(1, 10)
        densGet = random.randint(1, 10)
        blockGet = random.randint(1, 10)
        countGet = random.randint(1, 9)
        generateCity(streetGet, heightGet, densGet, blockGet, countGet)

#MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN
def generateCity(streetSize, buildHeight, buildDens, blockSize, blockCount):
    print ("here are the selected values")
    print (streetSize, buildHeight, buildDens, blockSize,blockCount)
    randomHeight = buildHeight
    heightFloat = float(buildHeight)
    
    for w in range(0,blockCount):
        cmds.group( em=True, name='block'+str(w))
        for y in range(0,4):
            rotation =90*y
            cmds.group( em=True, name='street'+str(w)+str(y) )
            for x in range(0,blockSize):
                randomHeight = random.randint(1, buildHeight)
                heightFloat = float(randomHeight)
                
                building = cmds.polyCube(width=3, height=randomHeight, depth=3, sx=6, sy=3, sz=6)
                cmds.move(x*(buildDens+3), heightFloat/2, 0)
                if (randomHeight==1):
                    cmds.select(building[0] + ".f[127]", building[0] + ".f[135]", building[0] + ".f[136]")
                    cmds.polyExtrudeFacet(translate =(0.15,0,0))
                    cmds.select(building[0] + ".f[7]", building[0] + ".f[8]", building[0] + ".f[9]",building[0] + ".f[10]")
                    cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                    cmds.select(building[0] + ".f[118]",building[0] + ".f[117]",building[0] + ".f[116]",building[0] + ".f[115]")
                    cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                    cmds.select(building[0] + ".f[64]",building[0] + ".f[63]",building[0] + ".f[62]",building[0] + ".f[61]")
                    cmds.polyExtrudeFacet(translate =(0,0,0.15))
                    
                    cmds.select(building[0] + ".f[45]", building[0] + ".f[40]", building[0] + ".f[34]")
                    cmds.polyExtrudeFacet(translate =(0,0.15,0))
                    cmds.select(building[0] + ".f[46]",building[0] + ".f[25]",building[0] + ".f[26]",building[0] + ".f[31]")
                    cmds.polyExtrudeFacet(translate =(0,0.2,0))
                elif (randomHeight==2):
                    cmds.select(building[0] + ".f[127]", building[0] + ".f[135]", building[0] + ".f[136]")
                    cmds.polyExtrudeFacet(translate =(0.15,0,0))
                    cmds.select(building[0] + ".f[7]", building[0] + ".f[8]", building[0] + ".f[9]",building[0] + ".f[10]")
                    cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                    cmds.select(building[0] + ".f[118]",building[0] + ".f[117]",building[0] + ".f[116]",building[0] + ".f[115]")
                    cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                    cmds.select(building[0] + ".f[64]",building[0] + ".f[63]",building[0] + ".f[62]",building[0] + ".f[61]")
                    cmds.polyExtrudeFacet(translate =(0,0,0.15))
                    
                    cmds.select(building[0] + ".f[44]", building[0] + ".f[45]", building[0] + ".f[46]")
                    cmds.polyExtrudeFacet(translate =(0,0.15,0))
                    cmds.select(building[0] + ".f[25]",building[0] + ".f[26]",building[0] + ".f[27]",building[0] + ".f[31]")
                    cmds.polyExtrudeFacet(translate =(0,0.2,0))
                    
                elif (randomHeight==3):
                    cmds.select(building[0] + ".f[45]", building[0] + ".f[40]", building[0] + ".f[34]")
                    cmds.polyExtrudeFacet(translate =(0,0.15,0))
                    cmds.select(building[0] + ".f[46]",building[0] + ".f[25]",building[0] + ".f[26]",building[0] + ".f[31]")
                    cmds.polyExtrudeFacet(translate =(0,0.2,0))
                    
                    cmds.select(building[0] + ".f[112]", building[0] + ".f[111]",building[0] + ".f[110]", building[0] + ".f[109]")
                    cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                    cmds.select(building[0] + ".f[70]", building[0] + ".f[69]",building[0] + ".f[68]", building[0] + ".f[67]")
                    cmds.polyExtrudeFacet(translate =(0,0,0.15))
                    cmds.select(building[0] + ".f[127]", building[0] + ".f[128]",building[0] + ".f[129]", building[0] + ".f[130]")
                    cmds.polyExtrudeFacet(translate =(0.15,0,0))
                    cmds.select(building[0] + ".f[1]", building[0] + ".f[2]",building[0] + ".f[3]", building[0] + ".f[4]")
                    cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                    
                    cmds.select(building[0] + ".f[124]", building[0] + ".f[123]",building[0] + ".f[122]", building[0] + ".f[121]",building[0] + ".f[118]", building[0] + ".f[117]",building[0] + ".f[116]", building[0] + ".f[115]")
                    cmds.polyExtrudeFacet(translate =(0.15,0,0))
                    cmds.select(building[0] + ".f[58]", building[0] + ".f[57]",building[0] + ".f[56]", building[0] + ".f[55]",building[0] + ".f[64]", building[0] + ".f[63]",building[0] + ".f[62]", building[0] + ".f[61]")
                    cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                    cmds.select(building[0] + ".f[139]", building[0] + ".f[140]",building[0] + ".f[141]", building[0] + ".f[142]",building[0] + ".f[133]", building[0] + ".f[134]",building[0] + ".f[135]", building[0] + ".f[136]")
                    cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                    cmds.select(building[0] + ".f[13]", building[0] + ".f[14]",building[0] + ".f[15]", building[0] + ".f[16]",building[0] + ".f[7]", building[0] + ".f[8]",building[0] + ".f[9]", building[0] + ".f[10]")
                    cmds.polyExtrudeFacet(translate =(0,0,0.15))
                    
                elif (randomHeight==4):
                    cmds.select(building[0] + ".f[29]", building[0] + ".f[35]", building[0] + ".f[41]", building[0] + ".f[47]",building[0] + ".f[52]", building[0] + ".f[51]", building[0] + ".f[50]", building[0] + ".f[49]",building[0] + ".f[42]", building[0] + ".f[36]", building[0] + ".f[30]", building[0] + ".f[24]",building[0] + ".f[19]", building[0] + ".f[20]", building[0] + ".f[21]", building[0] + ".f[22]",building[0] + ".f[53]",building[0] + ".f[48]",building[0] + ".f[18]",building[0] + ".f[23]")
                    cmds.polyExtrudeFacet(translate =(0,0.15,0))
                    
                    cmds.select(building[0] + ".f[45]", building[0] + ".f[40]", building[0] + ".f[34]")
                    cmds.polyExtrudeFacet(translate =(0,0.15,0))
                    cmds.select(building[0] + ".f[46]",building[0] + ".f[25]",building[0] + ".f[26]",building[0] + ".f[31]")
                    cmds.polyExtrudeFacet(translate =(0,0.2,0))
                    
                    cmds.select(building[0] + ".f[113]", building[0] + ".f[111]",building[0] + ".f[110]", building[0] + ".f[108]")
                    cmds.polyExtrudeFacet(translate =(0.15,0,0))
                    cmds.select(building[0] + ".f[71]", building[0] + ".f[69]",building[0] + ".f[68]", building[0] + ".f[66]")
                    cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                    cmds.select(building[0] + ".f[126]", building[0] + ".f[128]",building[0] + ".f[129]", building[0] + ".f[131]")
                    cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                    cmds.select(building[0] + ".f[0]", building[0] + ".f[2]",building[0] + ".f[3]", building[0] + ".f[5]")
                    cmds.polyExtrudeFacet(translate =(0,0,0.15))
                    
                    cmds.select(building[0] + ".f[124]", building[0] + ".f[123]",building[0] + ".f[122]", building[0] + ".f[121]",building[0] + ".f[118]", building[0] + ".f[117]",building[0] + ".f[116]", building[0] + ".f[115]")
                    cmds.polyExtrudeFacet(translate =(0.15,0,0))
                    cmds.select(building[0] + ".f[58]", building[0] + ".f[57]",building[0] + ".f[56]", building[0] + ".f[55]",building[0] + ".f[64]", building[0] + ".f[63]",building[0] + ".f[62]", building[0] + ".f[61]")
                    cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                    cmds.select(building[0] + ".f[139]", building[0] + ".f[140]",building[0] + ".f[141]", building[0] + ".f[142]",building[0] + ".f[133]", building[0] + ".f[134]",building[0] + ".f[135]", building[0] + ".f[136]")
                    cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                    cmds.select(building[0] + ".f[13]", building[0] + ".f[14]",building[0] + ".f[15]", building[0] + ".f[16]",building[0] + ".f[7]", building[0] + ".f[8]",building[0] + ".f[9]", building[0] + ".f[10]")
                    cmds.polyExtrudeFacet(translate =(0,0,0.15))
                    
                elif (randomHeight==5):
                    cmds.select(building[0] + ".f[52]", building[0] + ".f[49]",building[0] + ".f[42]", building[0] + ".f[24]",building[0] + ".f[19]", building[0] + ".f[22]", building[0] + ".f[47]",building[0] + ".f[29]")
                    cmds.polyExtrudeFacet(translate =(0,0.3,0))
                    cmds.select(building[0] + ".f[20]", building[0] + ".f[21]", building[0] + ".f[36]", building[0] + ".f[30]", building[0] + ".f[51]", building[0] + ".f[50]", building[0] + ".f[35]", building[0] + ".f[41]")
                    cmds.polyExtrudeFacet(translate =(0,0.7,0))
                    
                    cmds.select(building[0] + ".f[124]", building[0] + ".f[123]",building[0] + ".f[122]", building[0] + ".f[121]",building[0] + ".f[118]", building[0] + ".f[117]",building[0] + ".f[116]", building[0] + ".f[115]")
                    cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                    cmds.select(building[0] + ".f[58]", building[0] + ".f[57]",building[0] + ".f[56]", building[0] + ".f[55]",building[0] + ".f[64]", building[0] + ".f[63]",building[0] + ".f[62]", building[0] + ".f[61]")
                    cmds.polyExtrudeFacet(translate =(0,0,0.15))
                    cmds.select(building[0] + ".f[139]", building[0] + ".f[140]",building[0] + ".f[141]", building[0] + ".f[142]",building[0] + ".f[133]", building[0] + ".f[134]",building[0] + ".f[135]", building[0] + ".f[136]")
                    cmds.polyExtrudeFacet(translate =(0.15,0,0))
                    cmds.select(building[0] + ".f[13]", building[0] + ".f[14]",building[0] + ".f[15]", building[0] + ".f[16]",building[0] + ".f[7]", building[0] + ".f[8]",building[0] + ".f[9]", building[0] + ".f[10]")
                    cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                    
                    cmds.select(building[0] + ".f[113]", building[0] + ".f[111]",building[0] + ".f[110]", building[0] + ".f[108]")
                    cmds.polyExtrudeFacet(translate =(0.15,0,0))
                    cmds.select(building[0] + ".f[71]", building[0] + ".f[69]",building[0] + ".f[68]", building[0] + ".f[66]")
                    cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                    cmds.select(building[0] + ".f[126]", building[0] + ".f[128]",building[0] + ".f[129]", building[0] + ".f[131]")
                    cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                    cmds.select(building[0] + ".f[0]", building[0] + ".f[2]",building[0] + ".f[3]", building[0] + ".f[5]")
                    cmds.polyExtrudeFacet(translate =(0,0,0.15))
                    
                elif (randomHeight==6):
                    cmds.select(building[0] + ".f[29]", building[0] + ".f[35]", building[0] + ".f[41]", building[0] + ".f[47]",building[0] + ".f[52]", building[0] + ".f[51]", building[0] + ".f[50]", building[0] + ".f[49]",building[0] + ".f[42]", building[0] + ".f[36]", building[0] + ".f[30]", building[0] + ".f[24]",building[0] + ".f[19]", building[0] + ".f[20]", building[0] + ".f[21]", building[0] + ".f[22]",building[0] + ".f[53]",building[0] + ".f[48]",building[0] + ".f[18]",building[0] + ".f[23]")
                    cmds.polyExtrudeFacet(translate =(0,0.15,0))
                    
                    cmds.select(building[0] + ".f[124]", building[0] + ".f[123]",building[0] + ".f[122]", building[0] + ".f[121]",building[0] + ".f[118]", building[0] + ".f[117]",building[0] + ".f[116]", building[0] + ".f[115]")
                    cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                    cmds.select(building[0] + ".f[58]", building[0] + ".f[57]",building[0] + ".f[56]", building[0] + ".f[55]",building[0] + ".f[64]", building[0] + ".f[63]",building[0] + ".f[62]", building[0] + ".f[61]")
                    cmds.polyExtrudeFacet(translate =(0,0,0.15))
                    cmds.select(building[0] + ".f[139]", building[0] + ".f[140]",building[0] + ".f[141]", building[0] + ".f[142]",building[0] + ".f[133]", building[0] + ".f[134]",building[0] + ".f[135]", building[0] + ".f[136]")
                    cmds.polyExtrudeFacet(translate =(0.15,0,0))
                    cmds.select(building[0] + ".f[13]", building[0] + ".f[14]",building[0] + ".f[15]", building[0] + ".f[16]",building[0] + ".f[7]", building[0] + ".f[8]",building[0] + ".f[9]", building[0] + ".f[10]")
                    cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                    
                elif (randomHeight==7):
                    cmds.select(building[0] + ".f[29]", building[0] + ".f[35]", building[0] + ".f[41]", building[0] + ".f[47]",building[0] + ".f[52]", building[0] + ".f[51]", building[0] + ".f[50]", building[0] + ".f[49]",building[0] + ".f[42]", building[0] + ".f[36]", building[0] + ".f[30]", building[0] + ".f[24]",building[0] + ".f[19]", building[0] + ".f[20]", building[0] + ".f[21]", building[0] + ".f[22]")
                    cmds.polyExtrudeFacet(translate =(0,0.3,0))
                    cmds.select(building[0] + ".f[43]", building[0] + ".f[37]", building[0] + ".f[31]", building[0] + ".f[25]",building[0] + ".f[26]", building[0] + ".f[27]", building[0] + ".f[28]", building[0] + ".f[34]",building[0] + ".f[40]", building[0] + ".f[46]", building[0] + ".f[45]", building[0] + ".f[44]")
                    cmds.polyExtrudeFacet(translate =(0,1,0))
                    cmds.select(building[0] + ".f[33]", building[0] + ".f[32]", building[0] + ".f[38]", building[0] + ".f[39]")
                    cmds.polyExtrudeFacet(translate =(0,1.5,0))
                    
                    cmds.select(building[0] + ".f[124]", building[0] + ".f[123]",building[0] + ".f[122]", building[0] + ".f[121]",building[0] + ".f[118]", building[0] + ".f[117]",building[0] + ".f[116]", building[0] + ".f[115]")
                    cmds.polyExtrudeFacet(translate =(0.15,0,0))
                    cmds.select(building[0] + ".f[58]", building[0] + ".f[57]",building[0] + ".f[56]", building[0] + ".f[55]",building[0] + ".f[64]", building[0] + ".f[63]",building[0] + ".f[62]", building[0] + ".f[61]")
                    cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                    cmds.select(building[0] + ".f[139]", building[0] + ".f[140]",building[0] + ".f[141]", building[0] + ".f[142]",building[0] + ".f[133]", building[0] + ".f[134]",building[0] + ".f[135]", building[0] + ".f[136]")
                    cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                    cmds.select(building[0] + ".f[13]", building[0] + ".f[14]",building[0] + ".f[15]", building[0] + ".f[16]",building[0] + ".f[7]", building[0] + ".f[8]",building[0] + ".f[9]", building[0] + ".f[10]")
                    cmds.polyExtrudeFacet(translate =(0,0,0.15))
                    
                elif (randomHeight==8):
                    cmds.select(building[0] + ".f[52]", building[0] + ".f[49]",building[0] + ".f[42]", building[0] + ".f[24]",building[0] + ".f[19]", building[0] + ".f[22]", building[0] + ".f[47]",building[0] + ".f[29]")
                    cmds.polyExtrudeFacet(translate =(0,0.3,0))
                    cmds.select(building[0] + ".f[20]", building[0] + ".f[21]", building[0] + ".f[36]", building[0] + ".f[30]", building[0] + ".f[51]", building[0] + ".f[50]", building[0] + ".f[35]", building[0] + ".f[41]")
                    cmds.polyExtrudeFacet(translate =(0,0.7,0))
                    
                    cmds.select(building[0] + ".f[127]", building[0] + ".f[135]", building[0] + ".f[136]")
                    cmds.polyExtrudeFacet(translate =(0.15,0,0))
                    cmds.select(building[0] + ".f[7]", building[0] + ".f[8]", building[0] + ".f[9]",building[0] + ".f[10]")
                    cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                    cmds.select(building[0] + ".f[118]",building[0] + ".f[117]",building[0] + ".f[116]",building[0] + ".f[115]")
                    cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                    cmds.select(building[0] + ".f[64]",building[0] + ".f[63]",building[0] + ".f[62]",building[0] + ".f[61]")
                    cmds.polyExtrudeFacet(translate =(0,0,0.15))
                    
                elif (randomHeight==9):
                    cmds.select(building[0] + ".f[29]", building[0] + ".f[35]", building[0] + ".f[41]", building[0] + ".f[47]",building[0] + ".f[52]", building[0] + ".f[51]", building[0] + ".f[50]", building[0] + ".f[49]",building[0] + ".f[42]", building[0] + ".f[36]", building[0] + ".f[30]", building[0] + ".f[24]",building[0] + ".f[19]", building[0] + ".f[20]", building[0] + ".f[21]", building[0] + ".f[22]",building[0] + ".f[53]",building[0] + ".f[48]",building[0] + ".f[18]",building[0] + ".f[23]")
                    cmds.polyExtrudeFacet(translate =(0,0.15,0))
                    
                    cmds.select(building[0] + ".f[124]", building[0] + ".f[123]",building[0] + ".f[122]", building[0] + ".f[121]",building[0] + ".f[118]", building[0] + ".f[117]",building[0] + ".f[116]", building[0] + ".f[115]")
                    cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                    cmds.select(building[0] + ".f[58]", building[0] + ".f[57]",building[0] + ".f[56]", building[0] + ".f[55]",building[0] + ".f[64]", building[0] + ".f[63]",building[0] + ".f[62]", building[0] + ".f[61]")
                    cmds.polyExtrudeFacet(translate =(0,0,0.15))
                    cmds.select(building[0] + ".f[139]", building[0] + ".f[140]",building[0] + ".f[141]", building[0] + ".f[142]",building[0] + ".f[133]", building[0] + ".f[134]",building[0] + ".f[135]", building[0] + ".f[136]")
                    cmds.polyExtrudeFacet(translate =(0.15,0,0))
                    cmds.select(building[0] + ".f[13]", building[0] + ".f[14]",building[0] + ".f[15]", building[0] + ".f[16]",building[0] + ".f[7]", building[0] + ".f[8]",building[0] + ".f[9]", building[0] + ".f[10]")
                    cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                    
                elif (randomHeight==10):
                    cmds.select(building[0] + ".f[29]", building[0] + ".f[35]", building[0] + ".f[41]", building[0] + ".f[47]",building[0] + ".f[52]", building[0] + ".f[51]", building[0] + ".f[50]", building[0] + ".f[49]",building[0] + ".f[42]", building[0] + ".f[36]", building[0] + ".f[30]", building[0] + ".f[24]",building[0] + ".f[19]", building[0] + ".f[20]", building[0] + ".f[21]", building[0] + ".f[22]")
                    cmds.polyExtrudeFacet(translate =(0,0.3,0))
                    cmds.select(building[0] + ".f[43]", building[0] + ".f[37]", building[0] + ".f[31]", building[0] + ".f[25]",building[0] + ".f[26]", building[0] + ".f[27]", building[0] + ".f[28]", building[0] + ".f[34]",building[0] + ".f[40]", building[0] + ".f[46]", building[0] + ".f[45]", building[0] + ".f[44]")
                    cmds.polyExtrudeFacet(translate =(0,1,0))
                    cmds.select(building[0] + ".f[33]", building[0] + ".f[32]", building[0] + ".f[38]", building[0] + ".f[39]")
                    cmds.polyExtrudeFacet(translate =(0,1.5,0))
                    
                    cmds.select(building[0] + ".f[127]", building[0] + ".f[135]", building[0] + ".f[136]")
                    cmds.polyExtrudeFacet(translate =(0.15,0,0))
                    cmds.select(building[0] + ".f[7]", building[0] + ".f[8]", building[0] + ".f[9]",building[0] + ".f[10]")
                    cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                    cmds.select(building[0] + ".f[118]",building[0] + ".f[117]",building[0] + ".f[116]",building[0] + ".f[115]")
                    cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                    cmds.select(building[0] + ".f[64]",building[0] + ".f[63]",building[0] + ".f[62]",building[0] + ".f[61]")
                    cmds.polyExtrudeFacet(translate =(0,0,0.15))
                    
                cmds.group( building[0], parent='street'+str(w)+str(y))
                
                streetLight = cmds.polyCube(width=0.1, height=1.2, depth=0.1, sx=0, sy=14, sz=0)
                cmds.move(x*(buildDens+3), 1.2/2, 2)
                cmds.select(streetLight[0] + ".f[13]")
                cmds.polyExtrudeFacet(translate =(0,0,0.3))
                cmds.group( streetLight[0], parent='street'+str(w)+str(y))
            
                street = cmds.polyPlane(width=3*blockSize+(buildDens*blockSize)+blockSize*buildDens+6, height=1*streetSize*2, sx=streetSize*2, sy=streetSize*2)
                cmds.move((3*blockSize + (buildDens*blockSize))/2, 0, 3+(streetSize-1))
                #(3*blockSize+((buildDens*blockSize)-(buildDens*4)))/2
                cmds.group( street[0], parent='street'+str(w)+str(y))
                
                sideWalk = cmds.polyPlane(width=3*blockSize+(buildDens*blockSize)+4, height=0.5, sx=1, sy=1)
                cmds.move((3*blockSize + (buildDens*blockSize))/2, 0, 1.75)
                cmds.select(sideWalk[0] + ".f[1]")
                cmds.polyExtrudeFacet(translate =(0,0.07,0))
                cmds.group( sideWalk[0], parent='street'+str(w)+str(y))
            
            trafficLight = cmds.polyCube(width=0.1, height=1.2, depth=0.1, sx=0, sy=14, sz=0)
            cmds.select(trafficLight[0])
            cmds.move((x+2)*(buildDens+3)-(buildDens+1), 1.2/2, 2)
            cmds.select(trafficLight[0] + ".f[13]")
            cmds.polyExtrudeFacet(translate =(0,0,1))
            cmds.group(trafficLight[0], parent='street'+str(w)+str(y))
                
            cmds.rotate( 0, str(rotation)+'deg', 0, 'street'+str(w)+str(y) )
            if (y >=3):
                cmds.select('street'+str(w)+str(1))
                cmds.move(3*blockSize+(buildDens*blockSize),0,0)
                cmds.select('street'+str(w)+str(2))
                cmds.move((3*blockSize+(buildDens*blockSize)),0,-(3*blockSize+(buildDens*blockSize)))
                cmds.select('street'+str(w)+str(3))
                cmds.move(0,0,-(3*blockSize+(buildDens*blockSize)))
                
                cmds.group( 'street'+str(w)+str(0), parent='block'+str(w))
                cmds.group( 'street'+str(w)+str(1), parent='block'+str(w))
                cmds.group( 'street'+str(w)+str(2), parent='block'+str(w))
                cmds.group( 'street'+str(w)+str(3), parent='block'+str(w))
            if(y==3):
                for i in range(0,blockSize-1):
                    for q in range(0,blockSize-1):
                        randomHeight = random.randint(1, buildHeight)
                        heightFloat = float(randomHeight)
                        
                        building = cmds.polyCube(width=3, height=randomHeight, depth=3, sx=6, sy=3, sz=6)
                        cmds.move(3+buildDens + q*(buildDens+3), heightFloat/2, (1+i) * (buildDens - 3 - (2*buildDens)))
                        
                        if (randomHeight==1):
                            cmds.select(building[0] + ".f[127]", building[0] + ".f[135]", building[0] + ".f[136]")
                            cmds.polyExtrudeFacet(translate =(0.15,0,0))
                            cmds.select(building[0] + ".f[7]", building[0] + ".f[8]", building[0] + ".f[9]",building[0] + ".f[10]")
                            cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                            cmds.select(building[0] + ".f[118]",building[0] + ".f[117]",building[0] + ".f[116]",building[0] + ".f[115]")
                            cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                            cmds.select(building[0] + ".f[64]",building[0] + ".f[63]",building[0] + ".f[62]",building[0] + ".f[61]")
                            cmds.polyExtrudeFacet(translate =(0,0,0.15))
                            
                            cmds.select(building[0] + ".f[45]", building[0] + ".f[40]", building[0] + ".f[34]")
                            cmds.polyExtrudeFacet(translate =(0,0.15,0))
                            cmds.select(building[0] + ".f[46]",building[0] + ".f[25]",building[0] + ".f[26]",building[0] + ".f[31]")
                            cmds.polyExtrudeFacet(translate =(0,0.2,0))
                        elif (randomHeight==2):
                            cmds.select(building[0] + ".f[127]", building[0] + ".f[135]", building[0] + ".f[136]")
                            cmds.polyExtrudeFacet(translate =(0.15,0,0))
                            cmds.select(building[0] + ".f[7]", building[0] + ".f[8]", building[0] + ".f[9]",building[0] + ".f[10]")
                            cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                            cmds.select(building[0] + ".f[118]",building[0] + ".f[117]",building[0] + ".f[116]",building[0] + ".f[115]")
                            cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                            cmds.select(building[0] + ".f[64]",building[0] + ".f[63]",building[0] + ".f[62]",building[0] + ".f[61]")
                            cmds.polyExtrudeFacet(translate =(0,0,0.15))
                            
                            cmds.select(building[0] + ".f[44]", building[0] + ".f[45]", building[0] + ".f[46]")
                            cmds.polyExtrudeFacet(translate =(0,0.15,0))
                            cmds.select(building[0] + ".f[25]",building[0] + ".f[26]",building[0] + ".f[27]",building[0] + ".f[31]")
                            cmds.polyExtrudeFacet(translate =(0,0.2,0))
                            
                        elif (randomHeight==3):
                            cmds.select(building[0] + ".f[45]", building[0] + ".f[40]", building[0] + ".f[34]")
                            cmds.polyExtrudeFacet(translate =(0,0.15,0))
                            cmds.select(building[0] + ".f[46]",building[0] + ".f[25]",building[0] + ".f[26]",building[0] + ".f[31]")
                            cmds.polyExtrudeFacet(translate =(0,0.2,0))
                            
                            cmds.select(building[0] + ".f[112]", building[0] + ".f[111]",building[0] + ".f[110]", building[0] + ".f[109]")
                            cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                            cmds.select(building[0] + ".f[70]", building[0] + ".f[69]",building[0] + ".f[68]", building[0] + ".f[67]")
                            cmds.polyExtrudeFacet(translate =(0,0,0.15))
                            cmds.select(building[0] + ".f[127]", building[0] + ".f[128]",building[0] + ".f[129]", building[0] + ".f[130]")
                            cmds.polyExtrudeFacet(translate =(0.15,0,0))
                            cmds.select(building[0] + ".f[1]", building[0] + ".f[2]",building[0] + ".f[3]", building[0] + ".f[4]")
                            cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                            
                            cmds.select(building[0] + ".f[124]", building[0] + ".f[123]",building[0] + ".f[122]", building[0] + ".f[121]",building[0] + ".f[118]", building[0] + ".f[117]",building[0] + ".f[116]", building[0] + ".f[115]")
                            cmds.polyExtrudeFacet(translate =(0.15,0,0))
                            cmds.select(building[0] + ".f[58]", building[0] + ".f[57]",building[0] + ".f[56]", building[0] + ".f[55]",building[0] + ".f[64]", building[0] + ".f[63]",building[0] + ".f[62]", building[0] + ".f[61]")
                            cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                            cmds.select(building[0] + ".f[139]", building[0] + ".f[140]",building[0] + ".f[141]", building[0] + ".f[142]",building[0] + ".f[133]", building[0] + ".f[134]",building[0] + ".f[135]", building[0] + ".f[136]")
                            cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                            cmds.select(building[0] + ".f[13]", building[0] + ".f[14]",building[0] + ".f[15]", building[0] + ".f[16]",building[0] + ".f[7]", building[0] + ".f[8]",building[0] + ".f[9]", building[0] + ".f[10]")
                            cmds.polyExtrudeFacet(translate =(0,0,0.15))
                            
                        elif (randomHeight==4):
                            cmds.select(building[0] + ".f[29]", building[0] + ".f[35]", building[0] + ".f[41]", building[0] + ".f[47]",building[0] + ".f[52]", building[0] + ".f[51]", building[0] + ".f[50]", building[0] + ".f[49]",building[0] + ".f[42]", building[0] + ".f[36]", building[0] + ".f[30]", building[0] + ".f[24]",building[0] + ".f[19]", building[0] + ".f[20]", building[0] + ".f[21]", building[0] + ".f[22]",building[0] + ".f[53]",building[0] + ".f[48]",building[0] + ".f[18]",building[0] + ".f[23]")
                            cmds.polyExtrudeFacet(translate =(0,0.15,0))
                            
                            cmds.select(building[0] + ".f[45]", building[0] + ".f[40]", building[0] + ".f[34]")
                            cmds.polyExtrudeFacet(translate =(0,0.15,0))
                            cmds.select(building[0] + ".f[46]",building[0] + ".f[25]",building[0] + ".f[26]",building[0] + ".f[31]")
                            cmds.polyExtrudeFacet(translate =(0,0.2,0))
                            
                            cmds.select(building[0] + ".f[113]", building[0] + ".f[111]",building[0] + ".f[110]", building[0] + ".f[108]")
                            cmds.polyExtrudeFacet(translate =(0.15,0,0))
                            cmds.select(building[0] + ".f[71]", building[0] + ".f[69]",building[0] + ".f[68]", building[0] + ".f[66]")
                            cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                            cmds.select(building[0] + ".f[126]", building[0] + ".f[128]",building[0] + ".f[129]", building[0] + ".f[131]")
                            cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                            cmds.select(building[0] + ".f[0]", building[0] + ".f[2]",building[0] + ".f[3]", building[0] + ".f[5]")
                            cmds.polyExtrudeFacet(translate =(0,0,0.15))
                            
                            cmds.select(building[0] + ".f[124]", building[0] + ".f[123]",building[0] + ".f[122]", building[0] + ".f[121]",building[0] + ".f[118]", building[0] + ".f[117]",building[0] + ".f[116]", building[0] + ".f[115]")
                            cmds.polyExtrudeFacet(translate =(0.15,0,0))
                            cmds.select(building[0] + ".f[58]", building[0] + ".f[57]",building[0] + ".f[56]", building[0] + ".f[55]",building[0] + ".f[64]", building[0] + ".f[63]",building[0] + ".f[62]", building[0] + ".f[61]")
                            cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                            cmds.select(building[0] + ".f[139]", building[0] + ".f[140]",building[0] + ".f[141]", building[0] + ".f[142]",building[0] + ".f[133]", building[0] + ".f[134]",building[0] + ".f[135]", building[0] + ".f[136]")
                            cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                            cmds.select(building[0] + ".f[13]", building[0] + ".f[14]",building[0] + ".f[15]", building[0] + ".f[16]",building[0] + ".f[7]", building[0] + ".f[8]",building[0] + ".f[9]", building[0] + ".f[10]")
                            cmds.polyExtrudeFacet(translate =(0,0,0.15))
                            
                        elif (randomHeight==5):
                            cmds.select(building[0] + ".f[52]", building[0] + ".f[49]",building[0] + ".f[42]", building[0] + ".f[24]",building[0] + ".f[19]", building[0] + ".f[22]", building[0] + ".f[47]",building[0] + ".f[29]")
                            cmds.polyExtrudeFacet(translate =(0,0.3,0))
                            cmds.select(building[0] + ".f[20]", building[0] + ".f[21]", building[0] + ".f[36]", building[0] + ".f[30]", building[0] + ".f[51]", building[0] + ".f[50]", building[0] + ".f[35]", building[0] + ".f[41]")
                            cmds.polyExtrudeFacet(translate =(0,0.7,0))
                            
                            cmds.select(building[0] + ".f[124]", building[0] + ".f[123]",building[0] + ".f[122]", building[0] + ".f[121]",building[0] + ".f[118]", building[0] + ".f[117]",building[0] + ".f[116]", building[0] + ".f[115]")
                            cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                            cmds.select(building[0] + ".f[58]", building[0] + ".f[57]",building[0] + ".f[56]", building[0] + ".f[55]",building[0] + ".f[64]", building[0] + ".f[63]",building[0] + ".f[62]", building[0] + ".f[61]")
                            cmds.polyExtrudeFacet(translate =(0,0,0.15))
                            cmds.select(building[0] + ".f[139]", building[0] + ".f[140]",building[0] + ".f[141]", building[0] + ".f[142]",building[0] + ".f[133]", building[0] + ".f[134]",building[0] + ".f[135]", building[0] + ".f[136]")
                            cmds.polyExtrudeFacet(translate =(0.15,0,0))
                            cmds.select(building[0] + ".f[13]", building[0] + ".f[14]",building[0] + ".f[15]", building[0] + ".f[16]",building[0] + ".f[7]", building[0] + ".f[8]",building[0] + ".f[9]", building[0] + ".f[10]")
                            cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                            
                            cmds.select(building[0] + ".f[113]", building[0] + ".f[111]",building[0] + ".f[110]", building[0] + ".f[108]")
                            cmds.polyExtrudeFacet(translate =(0.15,0,0))
                            cmds.select(building[0] + ".f[71]", building[0] + ".f[69]",building[0] + ".f[68]", building[0] + ".f[66]")
                            cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                            cmds.select(building[0] + ".f[126]", building[0] + ".f[128]",building[0] + ".f[129]", building[0] + ".f[131]")
                            cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                            cmds.select(building[0] + ".f[0]", building[0] + ".f[2]",building[0] + ".f[3]", building[0] + ".f[5]")
                            cmds.polyExtrudeFacet(translate =(0,0,0.15))
                            
                        elif (randomHeight==6):
                            cmds.select(building[0] + ".f[29]", building[0] + ".f[35]", building[0] + ".f[41]", building[0] + ".f[47]",building[0] + ".f[52]", building[0] + ".f[51]", building[0] + ".f[50]", building[0] + ".f[49]",building[0] + ".f[42]", building[0] + ".f[36]", building[0] + ".f[30]", building[0] + ".f[24]",building[0] + ".f[19]", building[0] + ".f[20]", building[0] + ".f[21]", building[0] + ".f[22]",building[0] + ".f[53]",building[0] + ".f[48]",building[0] + ".f[18]",building[0] + ".f[23]")
                            cmds.polyExtrudeFacet(translate =(0,0.15,0))
                            
                            cmds.select(building[0] + ".f[124]", building[0] + ".f[123]",building[0] + ".f[122]", building[0] + ".f[121]",building[0] + ".f[118]", building[0] + ".f[117]",building[0] + ".f[116]", building[0] + ".f[115]")
                            cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                            cmds.select(building[0] + ".f[58]", building[0] + ".f[57]",building[0] + ".f[56]", building[0] + ".f[55]",building[0] + ".f[64]", building[0] + ".f[63]",building[0] + ".f[62]", building[0] + ".f[61]")
                            cmds.polyExtrudeFacet(translate =(0,0,0.15))
                            cmds.select(building[0] + ".f[139]", building[0] + ".f[140]",building[0] + ".f[141]", building[0] + ".f[142]",building[0] + ".f[133]", building[0] + ".f[134]",building[0] + ".f[135]", building[0] + ".f[136]")
                            cmds.polyExtrudeFacet(translate =(0.15,0,0))
                            cmds.select(building[0] + ".f[13]", building[0] + ".f[14]",building[0] + ".f[15]", building[0] + ".f[16]",building[0] + ".f[7]", building[0] + ".f[8]",building[0] + ".f[9]", building[0] + ".f[10]")
                            cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                            
                        elif (randomHeight==7):
                            cmds.select(building[0] + ".f[29]", building[0] + ".f[35]", building[0] + ".f[41]", building[0] + ".f[47]",building[0] + ".f[52]", building[0] + ".f[51]", building[0] + ".f[50]", building[0] + ".f[49]",building[0] + ".f[42]", building[0] + ".f[36]", building[0] + ".f[30]", building[0] + ".f[24]",building[0] + ".f[19]", building[0] + ".f[20]", building[0] + ".f[21]", building[0] + ".f[22]")
                            cmds.polyExtrudeFacet(translate =(0,0.3,0))
                            cmds.select(building[0] + ".f[43]", building[0] + ".f[37]", building[0] + ".f[31]", building[0] + ".f[25]",building[0] + ".f[26]", building[0] + ".f[27]", building[0] + ".f[28]", building[0] + ".f[34]",building[0] + ".f[40]", building[0] + ".f[46]", building[0] + ".f[45]", building[0] + ".f[44]")
                            cmds.polyExtrudeFacet(translate =(0,1,0))
                            cmds.select(building[0] + ".f[33]", building[0] + ".f[32]", building[0] + ".f[38]", building[0] + ".f[39]")
                            cmds.polyExtrudeFacet(translate =(0,1.5,0))
                            
                            cmds.select(building[0] + ".f[124]", building[0] + ".f[123]",building[0] + ".f[122]", building[0] + ".f[121]",building[0] + ".f[118]", building[0] + ".f[117]",building[0] + ".f[116]", building[0] + ".f[115]")
                            cmds.polyExtrudeFacet(translate =(0.15,0,0))
                            cmds.select(building[0] + ".f[58]", building[0] + ".f[57]",building[0] + ".f[56]", building[0] + ".f[55]",building[0] + ".f[64]", building[0] + ".f[63]",building[0] + ".f[62]", building[0] + ".f[61]")
                            cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                            cmds.select(building[0] + ".f[139]", building[0] + ".f[140]",building[0] + ".f[141]", building[0] + ".f[142]",building[0] + ".f[133]", building[0] + ".f[134]",building[0] + ".f[135]", building[0] + ".f[136]")
                            cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                            cmds.select(building[0] + ".f[13]", building[0] + ".f[14]",building[0] + ".f[15]", building[0] + ".f[16]",building[0] + ".f[7]", building[0] + ".f[8]",building[0] + ".f[9]", building[0] + ".f[10]")
                            cmds.polyExtrudeFacet(translate =(0,0,0.15))
                            
                        elif (randomHeight==8):
                            cmds.select(building[0] + ".f[52]", building[0] + ".f[49]",building[0] + ".f[42]", building[0] + ".f[24]",building[0] + ".f[19]", building[0] + ".f[22]", building[0] + ".f[47]",building[0] + ".f[29]")
                            cmds.polyExtrudeFacet(translate =(0,0.3,0))
                            cmds.select(building[0] + ".f[20]", building[0] + ".f[21]", building[0] + ".f[36]", building[0] + ".f[30]", building[0] + ".f[51]", building[0] + ".f[50]", building[0] + ".f[35]", building[0] + ".f[41]")
                            cmds.polyExtrudeFacet(translate =(0,0.7,0))
                            
                            cmds.select(building[0] + ".f[127]", building[0] + ".f[135]", building[0] + ".f[136]")
                            cmds.polyExtrudeFacet(translate =(0.15,0,0))
                            cmds.select(building[0] + ".f[7]", building[0] + ".f[8]", building[0] + ".f[9]",building[0] + ".f[10]")
                            cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                            cmds.select(building[0] + ".f[118]",building[0] + ".f[117]",building[0] + ".f[116]",building[0] + ".f[115]")
                            cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                            cmds.select(building[0] + ".f[64]",building[0] + ".f[63]",building[0] + ".f[62]",building[0] + ".f[61]")
                            cmds.polyExtrudeFacet(translate =(0,0,0.15))
                            
                        elif (randomHeight==9):
                            cmds.select(building[0] + ".f[29]", building[0] + ".f[35]", building[0] + ".f[41]", building[0] + ".f[47]",building[0] + ".f[52]", building[0] + ".f[51]", building[0] + ".f[50]", building[0] + ".f[49]",building[0] + ".f[42]", building[0] + ".f[36]", building[0] + ".f[30]", building[0] + ".f[24]",building[0] + ".f[19]", building[0] + ".f[20]", building[0] + ".f[21]", building[0] + ".f[22]",building[0] + ".f[53]",building[0] + ".f[48]",building[0] + ".f[18]",building[0] + ".f[23]")
                            cmds.polyExtrudeFacet(translate =(0,0.15,0))
                            
                            cmds.select(building[0] + ".f[124]", building[0] + ".f[123]",building[0] + ".f[122]", building[0] + ".f[121]",building[0] + ".f[118]", building[0] + ".f[117]",building[0] + ".f[116]", building[0] + ".f[115]")
                            cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                            cmds.select(building[0] + ".f[58]", building[0] + ".f[57]",building[0] + ".f[56]", building[0] + ".f[55]",building[0] + ".f[64]", building[0] + ".f[63]",building[0] + ".f[62]", building[0] + ".f[61]")
                            cmds.polyExtrudeFacet(translate =(0,0,0.15))
                            cmds.select(building[0] + ".f[139]", building[0] + ".f[140]",building[0] + ".f[141]", building[0] + ".f[142]",building[0] + ".f[133]", building[0] + ".f[134]",building[0] + ".f[135]", building[0] + ".f[136]")
                            cmds.polyExtrudeFacet(translate =(0.15,0,0))
                            cmds.select(building[0] + ".f[13]", building[0] + ".f[14]",building[0] + ".f[15]", building[0] + ".f[16]",building[0] + ".f[7]", building[0] + ".f[8]",building[0] + ".f[9]", building[0] + ".f[10]")
                            cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                            
                        elif (randomHeight==10):
                            cmds.select(building[0] + ".f[29]", building[0] + ".f[35]", building[0] + ".f[41]", building[0] + ".f[47]",building[0] + ".f[52]", building[0] + ".f[51]", building[0] + ".f[50]", building[0] + ".f[49]",building[0] + ".f[42]", building[0] + ".f[36]", building[0] + ".f[30]", building[0] + ".f[24]",building[0] + ".f[19]", building[0] + ".f[20]", building[0] + ".f[21]", building[0] + ".f[22]")
                            cmds.polyExtrudeFacet(translate =(0,0.3,0))
                            cmds.select(building[0] + ".f[43]", building[0] + ".f[37]", building[0] + ".f[31]", building[0] + ".f[25]",building[0] + ".f[26]", building[0] + ".f[27]", building[0] + ".f[28]", building[0] + ".f[34]",building[0] + ".f[40]", building[0] + ".f[46]", building[0] + ".f[45]", building[0] + ".f[44]")
                            cmds.polyExtrudeFacet(translate =(0,1,0))
                            cmds.select(building[0] + ".f[33]", building[0] + ".f[32]", building[0] + ".f[38]", building[0] + ".f[39]")
                            cmds.polyExtrudeFacet(translate =(0,1.5,0))
                            
                            cmds.select(building[0] + ".f[127]", building[0] + ".f[135]", building[0] + ".f[136]")
                            cmds.polyExtrudeFacet(translate =(0.15,0,0))
                            cmds.select(building[0] + ".f[7]", building[0] + ".f[8]", building[0] + ".f[9]",building[0] + ".f[10]")
                            cmds.polyExtrudeFacet(translate =(0,0,-0.15))
                            cmds.select(building[0] + ".f[118]",building[0] + ".f[117]",building[0] + ".f[116]",building[0] + ".f[115]")
                            cmds.polyExtrudeFacet(translate =(-0.15,0,0))
                            cmds.select(building[0] + ".f[64]",building[0] + ".f[63]",building[0] + ".f[62]",building[0] + ".f[61]")
                            cmds.polyExtrudeFacet(translate =(0,0,0.15))
                    
                        cmds.group( building[0], parent='street'+str(w)+str(y))
                    
        if(w==1 or w==2):
            cmds.select('block'+str(w))
            cmds.move(w*(3*blockSize+(buildDens*blockSize))+w*(3+((streetSize*2)+1)),0,0)
        elif(w==3 or w==4 or w==5):
            cmds.select('block'+str(w))
            cmds.move((w-3)*(3*blockSize+(buildDens*blockSize))+(w-3)*(3+((streetSize*2)+1)),0,1*(3*blockSize+(buildDens*blockSize))+1*(3+((streetSize*2)+1)))
        elif(w==6 or w==7 or w==8):
            cmds.select('block'+str(w))
            cmds.move((w-6)*(3*blockSize+(buildDens*blockSize))+(w-6)*(3+((streetSize*2)+1)),0,2*(3*blockSize+(buildDens*blockSize))+2*(3+((streetSize*2)+1)))