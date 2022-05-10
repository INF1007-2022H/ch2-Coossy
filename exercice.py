#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    new_mots=""
    for k in mot:
        new_mots += chr(ord(k)-32)
    return new_mots

if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
