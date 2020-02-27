import logging

def findSumOfK(s, k):
    ''' return whether any two numbers from the list s add up to k '''
    logging.debug(s)
    logging.debug(k)
    #create an empty set of compliments needed for reach K
    compList = set([])
    logging.debug(compList)

    #for each num a in s, see if k-a in in the compliment set
    for a in s:
        # if found, return true otherwise add the compliment
        comp = k-a   
        logging.debug(comp)

        if a in compList:
            logging.debug("Found Compliment")
            return True
        else:
            logging.debug("Adding Compliment To List")
            compList.add(comp)
            
    logging.debug("Compliment Not Found")
    return False

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    s = [10, 15, 3, 7]
    k = 17

    findSumOfK(s, k)

    