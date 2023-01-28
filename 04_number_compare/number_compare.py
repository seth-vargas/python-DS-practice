def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """

    if a == b:
        return "Numbers are equal"
    elif b > a:
        return "Second is greater"
    else:
        return "First is greater"

print(number_compare(1, 1))
print(number_compare(-1, 1))
print(number_compare(1, -2))