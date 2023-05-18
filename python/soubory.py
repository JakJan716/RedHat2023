from pathlib import Path


#1
def otevrit_soubor():
    obsah = []
    soubor = open(str(input("Napis cestu k souboru i s jeho koncovkou: ")))
    obsah = soubor.read()
    soubor.close()
    print(obsah)
#2
def otevrit_souborpasswd():
    obsah = []
    soubor = input("Zadej název souboru: ")
    x = Path(soubor).open("a")
    passwdsou = Path.open("/etc/passwd")
    lines = []
    for line in passwdsou.readlines():
        lines = line.split(":")
        x.write(f"Jmeno: {lines[0]} a bash: {lines[-1]}")

#    print(obsah)

#3
def zapis_soubor():
    soubor = Path(str(input("Napis cestu k souboru i s jeho koncovkou: ")))
    y = str(input("Sem napis co chces pripsat: "))
    pripsano = Path(soubor).open("a")
    pripsano.write(y)

otevrit_soubor()

#otevrit_souborpasswd()

#zapis_soubor()