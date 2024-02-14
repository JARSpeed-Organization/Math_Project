import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from PIL import Image, ImageTk

# Effectue un mélange Faro extérieur, en alternant les cartes des deux moitiés du paquet
def faro_out_shuffle(deck):
    half = len(deck) // 2  # Trouve le point médian du paquet
    # Crée un nouveau paquet en alternant les cartes des deux moitiés
    shuffled_deck = [val for pair in zip(deck[:half], deck[half:]) for val in pair]
    # Si le nombre de cartes est impair, ajoute la dernière carte à la fin
    if len(deck) % 2 != 0:
        shuffled_deck.append(deck[-1])
    return shuffled_deck

# Effectue un mélange Faro intérieur, en alternant les cartes avec la seconde moitié en premier
def faro_in_shuffle(deck):
    half = len(deck) // 2
    # Gère le cas d'un nombre impair de cartes
    second_half = deck[half:] if len(deck) % 2 == 0 else deck[half + 1:]
    first_half = deck[:half]
    shuffled_deck = []
    # Alterne les cartes à partir de la seconde moitié
    for i in range(max(len(first_half), len(second_half))):
        if i < len(second_half):
            shuffled_deck.append(second_half[i])
        if i < len(first_half):
            shuffled_deck.append(first_half[i])
    # Ajoute la carte du milieu au début pour un nombre impair de cartes
    if len(deck) % 2 != 0:
        shuffled_deck.insert(0, deck[half])
    return shuffled_deck


# Charge les images des cartes et les redimensionne
def load_card_images(deck_size):
    card_images = []
    for i in range(1, deck_size + 1):
        image = Image.open(f'../images2/{i}.png')  # Ouvre l'image de la carte
        image = image.resize((110, 159), Image.LANCZOS)  # Redimensionne l'image
        photo = ImageTk.PhotoImage(image)  # Convertit en format compatible avec Tkinter
        card_images.append(photo)  # Ajoute à la liste des images de cartes
    return card_images

# Affiche les cartes dans l'interface utilisateur
def display_cards(deck):
    for widget in frame_cards.winfo_children():
        widget.destroy()
    for i, card in enumerate(deck):
        row = i // 13
        column = i % 13
        # Crée un widget Label pour chaque carte et l'ajoute à la grille
        label = tk.Label(frame_cards, image=card_images[card - 1], bg='#ADD8E6')
        label.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
        frame_cards.grid_columnconfigure(column, weight=1)

# Demande la taille du paquet à l'utilisateur et initialise le paquet et les images
def set_deck_size():
    global deck_size, deck, card_images
    deck_size = simpledialog.askinteger("Taille du deck", "Avec combien de cartes voulez-vous jouer ?", minvalue=2, maxvalue=52)
    deck = list(range(1, deck_size + 1))  # Crée un paquet de la taille spécifiée
    card_images = load_card_images(deck_size)  # Charge les images des cartes
    display_cards(deck)


# Mélange le paquet selon le type spécifié et affiche le résultat
def shuffle_and_display(shuffle_type):
    global deck
    deck = faro_in_shuffle(deck) if shuffle_type == 'in' else faro_out_shuffle(deck)
    display_cards(deck)

# Fonction pour demander le nombre de cartes
def get_deck_size():
    return simpledialog.askinteger("Taille du deck", "Avec combien de cartes voulez-vous jouer ?", minvalue=2,
                                   maxvalue=52)
# Fonction pour trouver le nombre de mélanges pour revenir à l'état initial du paquet de carte
def calculate_shuffles(deck_size):

    k = 1
    while True:
        if (2 ** k - 1) % (deck_size - 1) == 0:
            return k
        k += 1

    return "Non défini pour ce nombre de cartes"

def calculate_shuffles_to_position(deck_size, target_position) :
    # Convertit la position cible en binaire pour déterminer la séquence de mélanges
    binary_position = bin(target_position - 1)[2:]  # Ignore le préfixe '0b'
    shuffle_sequence = []
    # Interprète chaque bit pour déterminer le type de mélange à effectuer
    for bit in binary_position:
        if bit == '1':
            shuffle_sequence.append('Faro In')
        else:
            shuffle_sequence.append('Faro Out')
    return shuffle_sequence

# Demande la position cible pour la première carte et affiche la séquence de mélanges nécessaire
def move_first_card_to_position():
    global deck
    target_position = simpledialog.askinteger("Position de la carte", "À quelle position voulez-vous déplacer la première carte ?", minvalue=1, maxvalue=len(deck))
    if target_position:
        shuffle_sequence = calculate_shuffles_to_position(len(deck), target_position)
        shuffle_sequence_text = "\n".join(shuffle_sequence)
        messagebox.showinfo("Déplacement de la carte", f"Pour déplacer la première carte à la position {target_position}, vous devez effectuer les mélanges suivants :\n{shuffle_sequence_text}")


window = tk.Tk()
window.title("Faro Shuffle Simulator")
window.configure(bg='#2C3E50')

frame_controls = tk.Frame(window, bg='#2C3E50', pady=10)
frame_controls.pack(fill=tk.X)

ttk.Button(frame_controls, text="Set Deck Size", command=set_deck_size).pack(side=tk.LEFT, padx=10)
ttk.Button(frame_controls, text="Faro In Mélange", command=lambda: shuffle_and_display('in')).pack(side=tk.LEFT,
                                                                                                   padx=10)
ttk.Button(frame_controls, text="Faro Out Mélange", command=lambda: shuffle_and_display('out')).pack(side=tk.LEFT,
                                                                                                     padx=10)
ttk.Button(frame_controls, text="Calculer mélanges nécessaires",
           command=lambda: messagebox.showinfo("Mélanges nécessaires",
                                               f"Nombre de mélanges nécessaire pour revenir au deck initial avec faro out: {calculate_shuffles(deck_size)}")).pack(
    side=tk.LEFT, padx=10)
ttk.Button(frame_controls, text="Déplacer première carte", command=move_first_card_to_position).pack(side=tk.LEFT, padx=10)

frame_cards = tk.Frame(window, bg='#ADD8E6')  # Set frame background to light blue
frame_cards.pack(expand=True, fill='both', padx=20, pady=20)

window.mainloop()