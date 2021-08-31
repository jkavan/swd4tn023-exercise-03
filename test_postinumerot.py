#!/bin/python3

from postinumerot import etsi_postinumero, vertaile_merkkijonoja

postinumerot = {
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI",
    "65374": "SMART POST",
    "74704": "SMARTPOST",
}

def test_etsi_yksi_postinumero():
    osumat = etsi_postinumero("Kiuruvesi", postinumerot)
    assert len(osumat) == 2

def test_etsi_useampi_postinumero():
    osumat = etsi_postinumero("MUURUVESI", postinumerot)
    assert len(osumat) == 1

def test_vertaile_merkkijonoja_samankaltaiset():
    assert vertaile_merkkijonoja("MUURUVESI", "muuruves") == True
    assert vertaile_merkkijonoja("SMARTPOST", "smart post") == True
    assert vertaile_merkkijonoja("SMARTPOST", "smart-post") == True
    assert vertaile_merkkijonoja("SMARTPOST", "smart posti") == True

def test_vertaile_merkkijonoja_yhteentormaykset():
    assert vertaile_merkkijonoja("kiuruvesi", "MUURUVESI") == False

test_etsi_yksi_postinumero()
test_etsi_useampi_postinumero()
test_vertaile_merkkijonoja_samankaltaiset()
test_vertaile_merkkijonoja_yhteentormaykset()
