#coding:utf-8
import unittest
import random

class Choice(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):

        element = random.choice(self.seq)
        self.assertTrue(element in self.seq,'buzai')


class Shuffle(unittest.TestCase):

    def setUp(self):
        self.seq = range(3)

    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq,range(3),'buyiyang')
        self.assertRaises(TypeError, range(3), (0,1,2))

if __name__ == '__main__':
    unittest.main()