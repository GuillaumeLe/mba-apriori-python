from itertools import chain, combinations
import itertools

def getDistinctElt(transactions):
    """
        Get the distinct element in a list of transactions.
    """
    distinctSet = set()
    for transaction in transactions:
        for elt in transaction:
            if not(elt in distinctSet):
                distinctSet.add(elt)
    return distinctSet

def getOccurence(item, transactions):
    """
        Get the number of occurence in a list of trnasactions
    """
    occurence = 0
    for transaction in transactions:
        for elt in transaction:
            if elt == item:
                occurence += 1
    return occurence

def strToSet(string):
    """
        Convert a string into a set
    """
    ens = set()
    for char in string:
        ens.add(char)
    return ens

def setToStr(ens):
    """
        Convert a set into a string.
    """
    string = ""
    ens = sorted(ens)
    for elt in ens:
        string += str(elt)
    return string

def getSubset(iterable):
    """ Get all subset of iterable """
    xs = list(iterable)
    # note we return an iterator rather than a list
    subsets_tuple = list(chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1)))
    subsets = [set(sub) for sub in subsets_tuple]
    return subsets

def setRules(occurence, conf):
    """
    Formate the rules from the occurence table and conserve only rules with
    enought confidence.
    INPUT
        occurence (list) : the table of occurence
        conf : the target confidence
    OUTPUT
        a list of rules where a rules is defined (pre, post, conf) which
        means : pre => post with conf confidence.
    """

    rules = []
    for level in occurence[:0:-1]:
        for item in level:
            ens = strToSet(item[0])
            occ = item[1]
            for elt in getSubset(ens):
                if (set(elt) != set()) and (set(elt) != ens):
                    for ref in occurence[len(elt)-1]:
                        if set(elt) == strToSet(ref[0]):
                            occ_ref = ref[1]
                    confidence = occ/occ_ref
                    if confidence >= conf:
                        rules.append((set(elt), set(ens.difference(elt)), confidence))
    return rules
def getLabels(occurence_dict):
    """
    Get the associations in occurence_dict without occurence
    INPUT
        occurence_dict (list) : contains the associations and occurence
    OUTPUT
        a list of the associations in occurence_dict
    """
    labels = []
    for elt in occurence_dict:
        labels.append(elt[0])
    return labels

def apriori(transactions, min_supp=3, confidence=0.75):
    """
    Run the apriori algorithme to found rules.
    INPUT
        transactions (list) : is a list of transactions wich is list of items.
        min_supp (int) : is the minimal support to consider a rules.
        confidence (float) : is the minimal confidence to consider a rules.
    OUTPUT
        A list of rules where each item contains (pre, post, confidence).
    """
    # get the distinct elt in transactions
    disctinct_elt = getDistinctElt(transactions)

    # a list that contains the rules, occurence_dict[n-1] contains the rules of
    # length n
    occurence_dict = []

    # labels contains the the association of item that we have conserved.
    # labels[n-1] contains set of association with n items
    labels = []

    # get the rules of length 1
    occurence_dict_current = []
    for item in disctinct_elt:
        # get the occurence of the item in transactions
        occurence = getOccurence(item, transactions)
        if occurence >= min_supp:
            occurence_dict_current.append((item,occurence))
    occurence_dict.append(occurence_dict_current)
    print(occurence_dict)
    # We add the associations converded
    labels.append(set(getLabels(occurence_dict[-1])))
    print(labels)
    n = 2
    # if the last item of occurence_dict is empty we've finished the algorithme
    while occurence_dict[-1] != []:

        # Building the cartesian product of associations of n-1 element and 1
        # element.
        cart = []
        for i in itertools.product(labels[0], labels[n-2]):
            if strToSet(i[0]).intersection(strToSet(i[1])) == set() and not(strToSet(i[0]).union(strToSet(i[1])) in cart):
                cart.append(strToSet(i[0]).union(strToSet(i[1])))
        print(cart)
        # finding the occurence of association of n elements
        occurence_dict_current = []
        for item in cart:
            occurence = getOccurence(list(item), transactions)
            if occurence >= min_supp:
                occurence_dict_current.append((set_to_str(item),occurence))
        occurence_dict.append(occurence_dict_current)
        labels.append(set(getLabels(occurence_dict[-1])))
        n += 1

    # Once we have all the associations and their occurences we formate the
    # rules
    print(occurence_dict)
    rules = setRules(occurence_dict[:-1], confidence)

    return rules
