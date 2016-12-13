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
        self.assertEqual(
            getDistinctElt(transactions),
            set(['A','B','C','D','E','F','H'])
        )
        transactions = [
            ['A','B','C'],
            ['A','C','D']
        ]
        self.assertEqual(
            getDistinctElt(transactions),
            set(['A','B','C','D'])
        )

    def test_getOccurence(self):
        transactions = [
            ['A','B','D','E'],
            ['C','A','D','B','F'],
            ['D','A','H','B','C'],
            ['E','F','B','C','E']
        ]
        self.assertEqual(getOccurence('A',transactions),3)
        self.assertEqual(getOccurence('H',transactions),1)
        self.assertEqual(getOccurence(set(['A','B']), transactions),3)

    def test_strToSet(self):
        self. assertEqual(strToSet("ABC"), set(['A','B','C']))
        self. assertEqual(strToSet("ABDE"), set(['A','B','E','D']))

    def test_setToStr(self):
        self.assertEqual(setToStr(set(['A', 'B', 'C'])), "ABC")
        self.assertEqual(setToStr(set(['D','B','C'])), 'BCD')

    def test_getSubset(self):
        ens = set(['A', 'B', 'C'])
        self.assertIn(set(['A']), getSubset(ens))
        self.assertIn(set(['B','C']), getSubset(ens))

    def test_setRules(self):
        occurence = [
            [
                ('A',3),
                ('B',4),
                ('C',3)
            ],
            [
                ('AB',3),
                ('AC',3),
                ('BC',3),
            ],
            [
                ('ABC',3)
            ]
        ]
        self.assertIn(
            (set(['A']),set(['B']),1), setRules(occurence, 0.75)
        )
        self.assertIn(
            (set(['B']),set(['A']),0.75), setRules(occurence, 0.75)
        )
        self.assertNotIn(
            (set(['B']),set(['A']),0.75), setRules(occurence, 0.8)
        )
        self.assertIn(
            (set(['A','B']),set(['C']),1), setRules(occurence, 0.75)
        )
    def test_getLabels(self):
        occurence_dict = [
            ('A',5),
            ('B',6),
            ('BC', 7),
            ('ABC', 4)
        ]
        self.assertIn('A', getLabels(occurence_dict))
        self.assertIn('BC', getLabels(occurence_dict))
        self.assertNotIn('AB', getLabels(occurence_dict))
        self.assertIn('ABC', getLabels(occurence_dict))
    def test_apriori(self):
        transactions = [
            ['A','B','D','E'],
            ['C','A','D','B','F'],
            ['D','A','H','B','C'],
            ['E','F','B','C']
        ]
        rules = apriori(transactions)
        self.assertIn(
            (set(['A']), set(['B']), 1),
            rules
        )
        self.assertIn(
            (set(['B']),set(['A','D']), 0.75),
            rules
        )
        self.assertIn(
            (set(['B']), set(['E']), 0.5),
            apriori(transactions, min_supp=2, confidence=0.5)
        )

if __name__ == "__main__":
    unittest.main()
