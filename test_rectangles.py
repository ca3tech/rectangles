import unittest
import rectangles as r

class test_rectangles(unittest.TestCase):

    def test_num_rectangles_square(self):
        self.assertEqual(r.num_rectangles([(0,0), (1,0), (0,1), (1,1)]), 1)

    def test_num_rectangles_diamond(self):
        self.assertEqual(r.num_rectangles([(0,1), (1,0), (2,1), (1,2)]), 1)

    def test_num_rectangles_3rec(self):
        points = []
        for x in range(0, 3):
            for y in range(0, 2):
                points.append((x,y))
        self.assertEqual(r.num_rectangles(points), 3)

    def test_num_rectangles_10rec(self):
        points = []
        for x in range(0, 3):
            for y in range(0, 3):
                points.append((x,y))
        self.assertEqual(r.num_rectangles(points), 10)

    def test_num_rectangles_20rec(self):
        points = []
        for x in range(0, 4):
            for y in range(0, 3):
                points.append((x,y))
        self.assertEqual(r.num_rectangles(points), 20)

if __name__ == "__main__":
    unittest.main()