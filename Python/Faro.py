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
deck = [f"{rank}{suit}" for suit in ["Carreau", "Cœur", "Trefle", "Pique"] for rank in ["AS de ","2 de ","3 de ","4 de ","5 de ","6 de ","7 de ","8 de ","9 de ","10 de ","Vallet de ","Dame de ","Roi de "]]
print("Jeu original:", deck,"\n")

shuffled_deck = faro_shuffle(deck)
print("Jeu mélangé:", shuffled_deck,"\n")
