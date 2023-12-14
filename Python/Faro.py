def faro_shuffle(deck):
    """Effectue un mélange Faro parfait sur un jeu de cartes."""
    half = len(deck) // 2
    shuffled_deck = []

    # Entrelacer les deux moitiés du jeu
    for i in range(half):
        shuffled_deck.append(deck[i])
        shuffled_deck.append(deck[i + half])

    return shuffled_deck

# Exemple d'utilisation avec un jeu de cartes standard
deck = [f"{rank}{suit}" for suit in "CDHS" for rank in "A23456789TJQK"]
print("Jeu original:", deck)

shuffled_deck = faro_shuffle(deck)
print("Jeu mélangé:", shuffled_deck)
