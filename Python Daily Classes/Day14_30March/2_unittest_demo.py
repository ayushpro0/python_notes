import unittest

# def my_func(a, 'ttest_ex.pyb') :
def my_func(a, b) :
    return a * b

#unittest.TestCase is a pre-defined class
class TestME(unittest.TestCase) : # TestME is a user defined class
    def setup(self):
        pass
    def testnum(self):
        self.assertEqual(my_func(3, 4), 12)
    
    def teststr(self):
        # self.assertEqual(my_func('a', 3), '3a') # Fail
        self.assertEqual(my_func('a', 3), 'aaa') # Pass

if __name__ == '__main__' :
    unittest.main() # transfers the control to TestME class
    # and executess testnum(), teststr() methods