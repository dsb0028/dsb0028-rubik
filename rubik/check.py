import rubik.cube as rubik
from collections import Counter

def _check(parms):
    result={}
    
    encodedCube = parms.get('cube',None)       
    isS = isinstance(encodedCube, str)
    
    color1 = encodedCube[4]
    color2 = encodedCube[31]
    color3 = encodedCube[49]
    color4 = encodedCube[22]
    color5 = encodedCube[13]
    color6 = encodedCube[40]    
    countColor1 = encodedCube.count(color1)
    countColor2  = encodedCube.count(color2)
    countColor3 = encodedCube.count(color3)
    countColor4 = encodedCube.count(color4)
    countColor5 = encodedCube.count(color5)
    countColor6 = encodedCube.count(color6)
    
   
    
    if (encodedCube != None) and (isS == True) and (len(encodedCube) == 54) and (countColor1 == countColor2 == countColor3 == countColor4 == countColor5 == countColor6 == 9) and (color1 != color2 != color3 != color4 != color5 != color6) :
        result['status'] = 'ok' 
        
    elif (encodedCube == None):
        result['status'] = 'error: cube is missing'
        
    elif (isS == False):
        result['status'] = 'error: cube is invalid'
        
    elif (len(encodedCube) < 54):
        result['status'] = 'error: cube is too short'

    elif (color1 == color2 or color1 == color3 or color1 == color2 or color1 == color3 or color1 == color4 or color1 == color5 or color1 == color6):
        result['status'] = 'error: cube is missing'
        
    elif (countColor1 != countColor2 != countColor3 != countColor4 != countColor5 != countColor6 != 9):
        result['status'] = 'error: cube is missing'
    return result

