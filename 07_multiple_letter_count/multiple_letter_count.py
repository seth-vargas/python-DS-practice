def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    letters = {}

    for letter in phrase:
        if letter in letters:
            letters[letter]+= 1
        else:
            letters[letter] = 1
    
    return letters

print(multiple_letter_count('yay')) # {'y': 2, 'a': 1}
print(multiple_letter_count('Yay')) # {'Y': 1, 'a': 1, 'y': 1}