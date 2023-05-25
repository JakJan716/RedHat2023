def obvodctverce(a):
    obvod = 4*a
    print(f"Obvod ctverce je: {obvod}")

def obsahctverce(a):
    obsah = a**2
    print(f"Obsah ctverce je: {obsah}")

def faktorial(a):
    faktorial = 1
    if int(a) >= 1:
        for i in range (1,a+1):
            faktorial = faktorial * i
    print(f"Faktorial čísla {a} vychází {faktorial}.")

a = int(input("Zadej stranu čtverce: "))

slovnik = {}

while True:
    klic = input("Zadej klic do slovniku: ")
    if klic == "":
        break
    else:
        hodnota = int(input("Zadej hodnotu k predeslemu klici: "))
        slovnik[klic] = hodnota

vyslsou = 0
for value in slovnik.values():
    vyslsou = vyslsou + value

print(f"Tohle je celkovy soucet ze slovniku: {vyslsou}")

#obvodctverce(a)
#obsahctverce(a)
#faktorial(a)