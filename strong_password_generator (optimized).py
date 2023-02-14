import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
password_vocabulary = letters + digits + special_chars

print('Hi! This program was made to generate strong passwords which contain letters, digits and special chars.')
length = input('Write down required password length (at least 12 symbols): ')


def generate(password=''):
    for i in range(int(length)):
        password += ''.join(secrets.choice(password_vocabulary))
    print('Your strong password is: ', password)


def generate_again():
    try:
        input('Press any key to generate new password...')
    except SyntaxError:
        generate()


while True:
    try:
        if int(length) < 12 or int(length) > 100:
            length = input('Invalid amount of symbols, try again: ')
            continue
        else:
            generate()
    except ValueError:
        length = input('Invalid type of input, try again: ')
        continue
    finally:
        generate_again()
