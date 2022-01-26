import rubik.cube as rubik
from collections import Counter

def _check(parms):
    result={}
    
    encodedCube = parms.get('cube',None)       
    isS = isinstance(encodedCube, str)
    countBlue = encodedCube.count('b')
    countRed  = encodedCube.count('r')
    countGreen = encodedCube.count('g')
    countOrange = encodedCube.count('o')
    countYellow = encodedCube.count('y')
    countWhite = encodedCube.count('w')
    blueFace = encodedCube[0:8]  #will only work if the cube is solved
    redFace = encodedCube[9:17]  #will only work if the cube is solved
    greenFace = encodedCube[18:26] #will only work if the cube is solved
    orangeFace = encodedCube[27:35] #will only work if the cube is solved 
    yellowFace = encodedCube[36:44] #will only work if the cube is solved
    whiteFace  = encodedCube[45:53] #will only work if the cube is solved
    
        
    if(encodedCube == None):
        result['status'] = 'error: cube is missing'
    elif (encodedCube != None) and (isS == True) and (len(encodedCube) == 54) and (countBlue == countRed == countGreen == countOrange == countWhite == countYellow == 9) and (whiteFace != blueFace != yellowFace != redFace != greenFace != orangeFace) :
        result['status'] = 'ok' 
    return result

