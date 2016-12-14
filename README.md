A python implementation of apriori algorithm for market basket analysis.
========================================================================

How to use apriori algorithm :
------------------------------

The algorithm is devloped for python 3.

Before using apriori algorithme, you have to clone the repository for instance
you can use `git clone https://github.com/GuillaumeLe/mba-apriori-python.git`
or you can download the .zip file and extract them in your project.

Next you have to include apriori in your python project : `import apriori`.

The apriori function use a liste of transactions, where each transaction is a
list of item.

    transactions = [
        ['A','B','D','E'],
        ['C','A','D','B','F'],
        ['D','A','H','B','C'],
        ['E','F','B','C']
    ]

Apriori function use three arguments `apriori(transactions)`:
* the transactions `transactions`.
* the minimum support `min_supp` which is the minimum number of occurence to
considere a case, by default `min_supp = 3`.
* the confidence `confidence`, by default `confidence = 0.75`

Development :
-------------

The librairy is develped with TDD method.
To run test use `python3 test.py`.
