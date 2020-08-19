#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random


password_length = int(input("Please enter the required password length: "))


def main(length=password_length):

    symbols = "1234567890QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"
    password = ""

    for i in range(password_length):
        password += random.choice(symbols)

    return password


if __name__ == "__main__":
    print(main())
