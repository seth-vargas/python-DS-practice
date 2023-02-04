def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("/Users/sethvargas/Desktop/Main/springboard/exercises/python-ds-practice/fs_5_read_file_list/dogs.txt")
        - Fido
        - Whiskey
        - Dr. Sniffle

        >>> read_file_list("/Users/sethvargas/Desktop/Main/springboard/exercises/python-ds-practice/fs_5_read_file_list/cats.txt")
        - Auden
        - Ezra
        - Fluffy
        - Meowsley

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!

    with open(filename) as file_name:
        for line in file_name:
            line = line.strip()
            print(f"- {line}")