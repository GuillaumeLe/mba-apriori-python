import unittest
from apriori import *
class AprioriTest(unittest.TestCase):
    def test_getDistinctElt(self):
        transactions = [
            ['A','B','D','E'], 
            ['C','A','D','B','F'], 
            ['D','A','H','B','C'], 
            ['E','F','B','C','E']
        ]
        self.assertEqual(getDistinctElt(transactions), set(['A','B','C','D','E','F','H']))
        transactions = [
            ['A','B','C'],
            ['A','C','D']
        ]
        self.assertEqual(getDistinctElt(transactions), set(['A','B','C','D']))
        
    def test_getOccurence(self):
        transactions = [
            ['A','B','D','E'], 
            ['C','A','D','B','F'], 
            ['D','A','H','B','C'], 
            ['E','F','B','C','E']
        ]
        self.assertEqual(getOccurence('A',transactions),3)
        self.assertEqual(getOccurence('H',transactions),1)
        
if __name__ == "__main__":
    unittest.main()
