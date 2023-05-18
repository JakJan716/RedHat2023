# Výzva: Pokédex

# Vytvořte třídu Pokémon, která bude reprezentovat jednoho pokémona.

class Pokemon:
    def __init__(self, jmeno: str, typ: str, uroven: int):
        self.jmeno = jmeno
        self.typ = typ
        self.uroven = uroven

    def __str__(self):
        return f"{self.jmeno} (typ: {self.typ}, úroveň: {self.uroven})"


# Vytvořte třídu Pokedex, která bude reprezentovat kolekci pokémonů.

class Pokedex:
    def __init__(self):
        self.pokemoni = []

    def pridej_pokemona(self, pokemon):
        self.pokemoni.append(pokemon)

    def vypis_pokemony(self):
        for pokemon in self.pokemoni:
            print(pokemon)


# Vytvořte funkci main, která bude obsahovat ukázkový kód.

def main():
    # Vytvoření instance Pokedexu
    pokedex = Pokedex()

    # Vytvoření několika Pokémonů
    x = str(input("Zadej jméno svého pokémona: ")) == Pokemon(str(input = jmeno), str(input = typ), int(input = uroven))

    # Přidání Pokémonů do Pokedexu
    pokedex.pridej_pokemona(pikachu)
    pokedex.pridej_pokemona(bulbasaur)
    pokedex.pridej_pokemona(charizard)

    # Výpis všech Pokémonů v Pokedexu
    pokedex.vypis_pokemony()


# Spuštění funkce main
if __name__ == "__main__":
    main()
