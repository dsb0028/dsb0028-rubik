import rubik.cube as rubik
from collections import Counter

def _eachFaceHasAColor(parms):
        encodedCube = parms.get('cube',None)    
        
def _check(parms):
    result={}
    
    
    encodedCube = parms.get('cube',None)       
    if (parms.get('cube') != None):
          
        if (isinstance(encodedCube, str) == True):

     
            if (encodedCube != None) and (len(encodedCube) == 54) and (encodedCube.count(encodedCube[49]) == encodedCube.count(encodedCube[4]) == encodedCube.count(encodedCube[13]) == encodedCube.count(encodedCube[31]) == encodedCube.count(encodedCube[22]) == encodedCube.count(encodedCube[40]) == 9) and (encodedCube[4] != encodedCube[13] != encodedCube[22] != encodedCube[31] != encodedCube[40]!= encodedCube[49]) :
                result['status'] = 'ok' 
       
        
            elif (len(encodedCube) < 54):
        
                result['status'] = 'error: cube is too short'
                
            elif (encodedCube.count(encodedCube[4]) != 9 or encodedCube.count(encodedCube[31]) != 9 or encodedCube.count(encodedCube[49]) != 9 or encodedCube.count(encodedCube[22]) != 9 or encodedCube.count(encodedCube[13]) != 9 or encodedCube.count(encodedCube[40]) != 9):
                result['status'] = 'error: cube must have 9 instances per color'

            elif (encodedCube[4] == encodedCube[31] or encodedCube[4] == encodedCube[49] or encodedCube[4] == encodedCube[22] or encodedCube[4] == encodedCube[13] or encodedCube[4] == encodedCube[40] or encodedCube[31] == encodedCube[49] or encodedCube[31] == encodedCube[22] or encodedCube[31] == encodedCube[13] or encodedCube[31] == encodedCube[40] or encodedCube[49] == encodedCube[22] or encodedCube[49] == encodedCube[13] or encodedCube[49] == encodedCube[40] or encodedCube[22] == encodedCube[13] or encodedCube[22] == encodedCube[40] or encodedCube[13] == encodedCube[40]):
                result['status'] = 'error: cube must have each middle face with a different color'
        
            return result

     
        else:
         result['status'] = 'error: cube is invalid'
         return result

    else:
      result['status'] = 'error: cube is missing'
      return result