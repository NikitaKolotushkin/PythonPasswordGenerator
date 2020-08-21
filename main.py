#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random  # Import random module


password_length = int(input("Please enter the required password length: "))  # Entering the password length


def main(length=password_length) -> str:
    """A function that generates a password"""

    symbols = "1234567890QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"  # Available Symbols
    password = ""

    for i in range(length):
        password += random.choice(symbols)

    return password


if __name__ == "__main__":
    print(main())