import string
import random


def upper_letter():
    letter = string.ascii_uppercase
    return letter


def lower_letter():
    letter = string.ascii_lowercase
    return letter


def digit_number():
    digit = string.digits
    return digit


def special_character():
    character = "~!@#$%^&*()-_=+[]{};:,.<>/?€£µ|"
    return character


def generatePassword(letters, length):
    letter = "".join(letters)
    password = []
    for _ in range(0, length):
        password.append(random.choice(letter))

    return "".join(password)