import itertools

def every_password(n: int) -> None:
    """
    Prints all possible passwords of length n, consisting of lowercase letters.

    Args:
        n (int): The length of the passwords.
    """

    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    passwords = itertools.product(lowercase_letters, repeat=n)

    for password in passwords:
        print(''.join(password))


print(every_password(4))