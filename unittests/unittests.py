'''
Created on Aug 22, 2013

@author: yuli
'''
import unittest
from game.grid import grid
from game import row_processor


class Test(unittest.TestCase):


    def setUp(self):
        self.grid = grid(5,5)
        self.grid.set_data(1, 1, 1)
        self.grid.set_data(2, 1, 1)
        self.grid.set_data(3, 1, 1)
        pass
    def testMath(self):
        patern = [[0,0,0,0,0], [0,0,0,0,0], [1,1,1,0,0], [0,0,0,0,0], [0,0,0,0,0]]
        idx = 0
        buf = grid(5,5)
        for row in self.grid._data:
            row_processor.process(self.grid, buf, row, idx)
            idx += 1
        for i in range(buf.rows):
            for j in range(buf.columns):
                self.assertEqual(buf.get_data(i, j), patern[i][j])
                    
    def tearDown(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()