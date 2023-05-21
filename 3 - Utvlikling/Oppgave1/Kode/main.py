

# oppg1()
def oppg1(tall_liste: list, str_liste: list) -> float:
    
    # Produkt er lik første tallet i tall_liste og skal returneres
    produkt: float = float(tall_liste[0])
    
    # For alle tall i tall_liste
    for round in range(0, len(tall_liste)):
        # Om det ikke er første runde. Dette gjøres pga. at første runde kjøres på linje 7
        if round != 0:
            # Produkt ganges med tall
            produkt *= tall_liste[round]

    # Legg til første str i produkt som en float
    produkt += float(str_liste[0])
    # Returner produkt
    return produkt


# Om koden kjører i det lokale skriptet
if __name__ == "__main__":
    # Kjør funksjonen med test verdier
    test = oppg1([2, 2, 4], ["1.2", "3.4", "2"])
    print("Test av programmet:",test)