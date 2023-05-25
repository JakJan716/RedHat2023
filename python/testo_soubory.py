import pytest
from pathlib import Path

def otevrit_soubor():
    obsah = []
    soubor = ("/home/JakJan716/jakub/RedHat2023/python/soubor.txt")
    obsah = Path(soubor).open("a")
    print(obsah)

def test_otevri_soubor():
    otevrit_soubor()
    