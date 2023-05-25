from pathlib import Path
import os

class soubory:

    def __init__(self, obsah, soubor,prepisovany_soubor, passwd_soubor, pripsano ):
        self.obsah = []
        self.soubor = input("Zadej svůj soubor: ")
        self.prepisovany_soubor = input("Zadej přepisovaný soubor: ")
        self.passwd_soubor = passwd_soubor
        self.pripsano = pripsano

    def otevrit_soubor(self):
        self.obsah = self.soubor.read()
        self.soubor.close()
        print(self.obsah)

    def otevrit_souborpasswd(self):
        self.prepisovany_soubor = Path(self.soubor).open("a")
        self.passwd_soubor = Path.open("/etc/passwd")
        lines = []
        for line in self.passwd_soubor.readlines():
            lines = line.split(":")
            self.prepisovany_soubor.write(f"Jmeno: {lines[0]} a bash: {lines[-1]}")

    def zapis_soubor(self):
        y = str(input("Sem napis co chces pripsat: "))
        self.pripsano = Path(self.soubor).open("a")
        self.pripsano.write(y)



soubory.otevrit_soubor(self)

#soubory.otevrit_souborpasswd()

#soubory.zapis_soubor()