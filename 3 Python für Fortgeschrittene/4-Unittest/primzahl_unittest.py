import unittest
from primzahl import ist_primzahl

class PrimzahlTest(unittest.TestCase):

    def testPrimzahl(self):
        self.assertEqual(ist_primzahl(0), True)
        self.assertEqual(ist_primzahl(1), True)
        self.assertEqual(ist_primzahl(10), False)
        self.assertEqual(ist_primzahl(15), False)

if __name__ == "__main__": 
    unittest.main()