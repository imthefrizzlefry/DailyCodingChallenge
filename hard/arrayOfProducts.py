import logging

''' This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

def arrayOfProducts(myArray):
    newArray = []
    prodBeforeI = 1
    prodAfterI = 1

    for num in myArray:
        prodAfterI *= num

    for i in range(0,len(myArray)):
        if i > 0:
            prodBeforeI *= myArray[i-1]
        prodAfterI /= myArray[i]
        newArray.append(int(prodBeforeI * prodAfterI))

    return newArray
    

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    a = [1,2,3,4,5]

    result = arrayOfProducts(a)
    logging.debug(result)