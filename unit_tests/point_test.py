import unittest
from point import Point

class testPoint(unittest.TestCase):
    '''here we test the Point class'''
    def setUp(self):
        '''this method will be executed before the tests are run'''
        self.point = Point(3,5) # a sensible instance for use in each test

    # declare some independent tests (setUp will run before each)
    def testMoveBy(self):
        self.point.moveBy(-5, -2)
        self.assertEqual(self.point.display(), (-2, 3) )
    def testMoveByXY(self):
        self.point.moveBy(5,2)
        self.assertEqual( self.point.x, 8 )
        self.assertEqual( self.point.y, 7 )
    def testRaises(self):
        with self.assertRaises(TypeError):
            self.point.moveBy('a', 'b')

if __name__ == '__main__':
    unittest.main() # invoke the tests