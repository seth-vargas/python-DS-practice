def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    phrase = list(phrase)
    copy = phrase.copy()
    phrase.reverse()

    if copy == phrase:
        return True
    return False

print(is_palindrome('tacocat'), True)
print(is_palindrome('noon'), True)
print(is_palindrome('robert'), False)