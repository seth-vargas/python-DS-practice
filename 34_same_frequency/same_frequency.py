def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    num_dict = {}

    list_of_nums = [int(i) for i in str(num1)] + [int(i) for i in str(num2)]

    for num in list_of_nums:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1

    for num in num_dict:
        if num_dict.get(num) % 2 != 0:
            return False
    return True