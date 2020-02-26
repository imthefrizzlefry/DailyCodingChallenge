def FindSumOfK(s, k):
    ''' return whether any two numbers from the list s add up to k '''
    #create an empty set of compliments needed for reach K
    compList = set()
    #for each num a in s, see if k-a in in the compliment set
    for a in s:
        # if found, return true otherwise add the compliment
        comp = k-a
        if comp in compList:
            return True
        else:
            compList.add(comp)

    return False