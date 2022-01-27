import rubik.cube as rubik
from collections import Counter

def _eachFaceHasAColor(parms):
     encodedCube = parms.get('cube',None)    
        
    
def _check(parms):
    result={}
    color1 = None
    color2 = None
    color3 = None
    color4 = None
    color5 = None
    color6 = None
    
    countColor1 = None
    countColor2  = None
    countColor3 = None
    countColor4 = None
    countColor5 = None
    countColor6 = None
    
    encodedCube = parms.get('cube',None)       
    isS = isinstance(encodedCube, str)
    
    if (len(encodedCube) <= 54 and len(encodedCube) >= 50):
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
        
        
    elif (len(encodedCube) < 50 and len(encodedCube) >= 41):   
         color1 = encodedCube[4]
         color2 = encodedCube[31]
         color4 = encodedCube[22]
         color5 = encodedCube[13]
         color6 = encodedCube[40]
         
         countColor1 = encodedCube.count(color1)
         countColor2  = encodedCube.count(color2)
         countColor4 = encodedCube.count(color4)
         countColor5 = encodedCube.count(color5)
         countColor6 = encodedCube.count(color6)
         
    elif (len(encodedCube) < 41 and len(encodedCube) >= 32):
         color1 = encodedCube[4]
         color2 = encodedCube[31]
         color4 = encodedCube[22]
         color5 = encodedCube[13]
         
         countColor1 = encodedCube.count(color1)
         countColor2  = encodedCube.count(color2)
         countColor4 = encodedCube.count(color4)
         countColor5 = encodedCube.count(color5)
         
    elif (len(encodedCube) < 32 and len(encodedCube) >= 23):
         color1 = encodedCube[4]
         color4 = encodedCube[22]
         color5 = encodedCube[13]
         
         countColor1 = encodedCube.count(color1)
         countColor4 = encodedCube.count(color4)
         countColor5 = encodedCube.count(color5)
    elif (len(encodedCube) < 23 and len(encodedCube) >= 14):
         color1 = encodedCube[4]
         color5 = encodedCube[13]       
         
         countColor1 = encodedCube.count(color1)
         countColor5 = encodedCube.count(color5)
         
    elif (len(encodedCube) < 14 and len(encodedCube) >= 5):
         color1 = encodedCube[4]    
   
         countColor1 = encodedCube.count(color1)
    
     
    if (encodedCube != None) and (isS == True) and (len(encodedCube) == 54) and (countColor1 == countColor2 == countColor3 == countColor4 == countColor5 == countColor6 == 9) and (color1 != color2 != color3 != color4 != color5 != color6) :
        result['status'] = 'ok' 
        
    elif (encodedCube == None):
        result['status'] = 'error: cube is missing'
        
    elif (isS == False):
        result['status'] = 'error: cube is invalid'
        
    elif (len(encodedCube) < 54):
        
        result['status'] = 'error: cube is too short'

    elif (color1 == color2 or color1 == color3 or color1 == color4 or color1 == color5 or color1 == color6 or color2 == color3 or color2 == color4 or color2 == color5 or color2 == color6 or color3 == color4 or color3 == color5 or color3 == color6 or color4 == color5 or color4 == color6 or color5 == color6):
        result['status'] = 'error: cube must have 6 distinct colors'
        
    elif (countColor1 != countColor2 != countColor3 != countColor4 != countColor5 != countColor6 != 9):
        result['status'] = 'error: cube must have 9 instances per color'
    return result

    


