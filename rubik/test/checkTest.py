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
        self.assertEqual(status, 'ok')
        
    def test_check_013_ShouldReturnErrorOnMixedCube(self):
        parm = {'op':'check'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
                 
    def test_check_014_ShouldReturnErrorOnMixedCube(self):
        parm = {'op':'check',
                'cube': 42}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    