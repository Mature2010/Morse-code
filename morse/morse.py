#!usr/bin/local/python3
# -*- coding: utf-8 -*-
import os

def main():
    dictionary = {
        'A' : '· —',
        'B' : '— · · ·',
        'C' : '— · — ·',
        'D' : '— · ·',
        'E' : '.',
        'F' : '· · — ·',
        'G' : '— — ·',
        'H' : '· · · ·',
        'I' : '· ·',
        'J' : '· — — —',
        'K' : '— · —',
        'L' : '· — · ·',
        'M' : '— —',
        'N' : '— ·',
        'Ñ' : '— — · — —',
        'O' : '— — —',
        'P' : '· — — ·',
        'Q' : '— — · —',
        'R' : '· — ·',
        'S' : '· · ·',
        'T' : '—',
        'U' : '· · —',
        'V' : '· · · —',
        'W' : '· — —',
        'X' : '— · · —',
        'Y' : '— · — —',
        'Z' : '— — · ·',
        '0' : '— — — — —',
        '1' : '· — — — —',
        '2' : '· · — — —',
        '3' : '· · · — —',
        '4' : '· · · · —',
        '5' : '· · · · ·',
        '6' : '— · · · ·',
        '7' : '— — · · ·',
        '8' : '— — — · ·',
        '9' : '— — — — ·',
        '.' : '· — · — · —',
        ',' : '— · — · — —',
        '?' : '· · — — · ·',
        '\"' : '· — · · — ·',
        '!' : '— — · · — —',
        ' ' : '/'
    }
    exit = 0

    while exit == 0:
        election = input("[T]ext to Morse\n[M]orse to Text\n[L]isten morse\n[E]xit\n-> ").upper()

        if election == 'T':
            text = input("Message:\n").upper()
            for key in text:
                print(f"{dictionary.get(key)}  ", end="")
        elif election == 'M':
            text = input("Message:\n")
            word = text.split("  ")
            for morse in word:
                for key, value in dictionary.items():
                    if value == morse:
                        print(f"{key}", end="")
        elif election == 'L':
            text = input("Message:\n")
            word = text.split(" ")
            print(word)
            for i in word:
                if i == "—":
                    os.system("mpv _.ogg")
                elif i == "·":
                    os.system("mpv p.ogg")
                else: pass
        elif election == 'E':
            exit = 1
        else:
            print("Option does not exist")

        print("\n")

if __name__ == '__main__':
    main()
