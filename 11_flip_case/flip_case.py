def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    phrase = list(phrase)
    lst = []

    for letter in phrase:
        if letter.upper() == to_swap.upper():
            lst.append(letter.swapcase())
        else:
            lst.append(letter)
            
    return ''.join(lst)


print(flip_case('Aaaahhh', 'a'), 'aAAAhhh')
print(flip_case('Aaaahhh', 'A'), 'aAAAhhh')
print(flip_case('Aaaahhh', 'h'), 'AaaaHHH')