from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):
        
    def test_check_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_check_011_ShouldReturnOkOnMixedCube(self):
        parm = {'op':'check',
                'cube':'11w11w11wrrrrrrrrryggyggyggaaaaaaaaayy1yy1yy1wwgwwgwwg'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_check_012_ShouldReturnErrorOnMixedCube(self):
        parm = {'op':'check',
                'cube':'123456789'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is too short')
        
    def test_check_013_ShouldReturnErrorOnMixedCube(self):
        parm = {'op':'check'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is missing')
                 
    def test_check_014_ShouldReturnErrorOnMixedCube(self):
        parm = {'op':'check',
                'cube': 42}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is invalid')
    def test_check_015_ShouldReturnErrorOnCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbbrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must have 9 instances per color')
        
    def test_check_016_ShouldReturnErrorOnMixedCube(self):
        #encodedCube[4] = 1
        #encodedCube[13] = 1
        #encodedCube[22] = g
        #encodedCube[31] = a
        #encodedCube[40] = y
        #encodedCube[49] = w
        parm = {'op':'check',
                'cube':'1rwr1w11wrrrr1rrr1yggyggyggaaaaaaaaayy1yy1yy1wwgwwgwwg'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube must have each middle face with a different color')
        