import pytest
from pathlib import Path

def otevrit_soubor():
    obsah = []
    soubor = ("usr/bin/ls")
    obsah = Path(soubor).open("a")
    print(obsah)

def test_otevri_soubor():
    otevrit_soubor()
    