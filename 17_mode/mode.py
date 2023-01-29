def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    myDict = {}
    count = 0
    mode = 0
    
    for num in nums:
        myDict[num] = myDict.get(num, 0) + 1
        if myDict[num] >= count:
            count = myDict[num]
            mode = num

    return mode

print(mode([1, 2, 1]), 1)
print(mode([2, 2, 3, 3, 2]), 2)