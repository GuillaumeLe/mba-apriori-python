def getDistinctElt(transactions):
    distinctSet = set()
    for transaction in transactions:
        for elt in transaction:
            if not(elt in distinctSet):
                distinctSet.add(elt)
    return distinctSet 

def getOccurence(elt, transactions):
    occurence = 0
    return 3
