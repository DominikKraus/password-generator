import string
import random
import argparse

parser = argparse.ArgumentParser(description='simple password generator')
parser.add_argument("-length")

args = parser.parse_args()
length = args.length
real_length = int(length)

def generate_password(length=10):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

print("\nYour random generated password is:")
print(generate_password(real_length) + "\n")