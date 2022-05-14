import unittest
import tkinter
from GUI import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.GUI = GUI(tkinter.Tk())

    def test__init__(self):
        window = tkinter.Tk()
        widgets = GUI(window)
        self.assertIsInstance(widgets, GUI)

    def test_clicked(self):
        self.GUI.var1.insert(0, '1')
        self.GUI.radio_1.set(0)

        self.GUI.clicked()
        expect = 1
        result = self.GUI.label.label.cget('text')
        self.assertEqual(expect, result)



        self.GUI.var1.insert(0, '2')
        self.GUI.var2.insert(0, '3')
        self.GUI.radio_1.set(1)

        self.GUI.clicked()
        expect = 8
        result = self.GUI.label.label.cget('text')
        self.assertEqual(expect, result)



        self.GUI.var1.insert(0, '3')
        self.GUI.radio_1.set(2)

        self.GUI.clicked()
        expect = '3 2 1'
        result = self.GUI.label.label.cget('text')
        self.assertEqual(expect, result)


    def test_adding(self):
        self.GUI.adding(3)
        result = self.GUI.label.label.cget('text')

        self.assertEqual(result, 6)


    def test_exponents(self):
        self.GUI.exponents(3, 2)
        result = self.GUI.label.label.cget('text')

        self.assertEqual(result, 9)


    def test_listing(self):
        self.GUI.listing(4)
        result = self.GUI.label.label.cget('text')

        self.assertEquals(result, '4 3 2 1')


if __name__ == '__main__':
    unittest.main()
