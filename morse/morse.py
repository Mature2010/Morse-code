#!usr/bin/local/python3
# -*- coding: utf-8 -*-
import os
from time import sleep

dictionary = {
    'A' : '. _',
    'B' : '_ . . .',
    'C' : '_ . _ .',
    'D' : '_ . .',
    'E' : '.',
    'F' : '. . _ .',
    'G' : '_ _ .',
    'H' : '. . . .',
    'I' : '. .',
    'J' : '. _ _ _',
    'K' : '_ . _',
    'L' : '. _ . .',
    'M' : '_ _',
    'N' : '_ .',
    'Ñ' : '_ _ . _ _',
    'O' : '_ _ _',
    'P' : '. _ _ .',
    'Q' : '_ _ . _',
    'R' : '. _ .',
    'S' : '. . .',
    'T' : '_',
    'U' : '. . _',
    'V' : '. . . _',
    'W' : '. _ _',
    'X' : '_ . . _',
    'Y' : '_ . _ _',
    'Z' : '_ _ . .',
    '0' : '_ _ _ _ _',
    '1' : '. _ _ _ _',
    '2' : '. . _ _ _',
    '3' : '. . . _ _',
    '4' : '. . . . _',
    '5' : '. . . . .',
    '6' : '_ . . . .',
    '7' : '_ _ . . .',
    '8' : '_ _ _ . .',
    '9' : '_ _ _ _ .',
    '.' : '. _ . _ . _',
    ',' : '_ . _ . _ _',
    '?' : '. . _ _ . .',
    '\"' : '. _ . . _ .',
    '!' : '_ _ . . _ _',
    ' ' : '/'
}

def grammar():
    for key, value in dictionary.items():
        print(f"{key} : {value}")

def encoder(text):
    message = ""
    for key in text.upper():
        message += dictionary.get(key) + "  "
    return message

def decoder(text):
    message = ""
    word = text.split("  ")
    for morse in word:
        for key, value in dictionary.items():
            if value == morse:
                message += key
    return message

def playMorse(text):
    word = text.split(" ")
    for i in word:
        if i == "_":
            os.system("mpv s.ogg")
        elif i == ".":
            os.system("mpv p.ogg")
        elif i == "/":
            sleep(.8)
        elif i == "":
            sleep(.4)
        else: pass

def main():
    exit = 0
    while exit == 0:
        election = input("\n[D]ictionary\n[T]ext to Morse\n[M]orse to Text\n[L]isten morse\n[E]xit\n-> ").upper()

        if election == 'D':
            grammar()
        elif election == 'T':
            text = input("Message:\n")
            print(encoder(text))
        elif election == 'M':
            text = input("Message:\n")
            print(decoder(text))
        elif election == 'L':
            text = input("Message:\n")
            playMorse(text)
        elif election == 'E':
            exit = 1
        else:
            print("Option does not exist")

if __name__ == '__main__':
    main()
