#!/bin/python3

import urllib.request
import Levenshtein
import json

def hae_postinumerot():
    """ Palauttaa listan postinumeroista ja -toimipaikoista """
    postinumerot = ""
    req = urllib.request.Request('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json')
    with urllib.request.urlopen(req) as response:
       postinumerot = response.read()
       postinumerot = json.loads(postinumerot)
    return postinumerot

def etsi_postinumero(postitoimipaikka, postinumerot):
    """ Palauttaa listasta postinumerot annetulle postitoimipaikalle """
    osumat = []
    for key, value in postinumerot.items():
        if vertaile_merkkijonoja(value, postitoimipaikka):
            osumat.append(key)
    return osumat

def vertaile_merkkijonoja(merkkijono1, merkkijono2):
    """ Palauttaa booleanin. Tarkistaa, ovatko merkkijonot riittävän samankaltaisia """
    merkkijono1 = merkkijono1.replace(" ", "").lower()
    merkkijono2 = merkkijono2.replace(" ", "").lower()
    return (Levenshtein.distance(merkkijono1, merkkijono2) <= 1)

def main():
    postinumerot = hae_postinumerot()
    postitoimipaikka = ""
    while len(postitoimipaikka) < 1:
        postitoimipaikka = input('Kirjoita postitoimipaikka: ')

    osumat = etsi_postinumero(postitoimipaikka, postinumerot)
    print("Postinumerot:", end = " ")
    print(*osumat, sep = ', ')

if __name__ == '__main__':
    main()
