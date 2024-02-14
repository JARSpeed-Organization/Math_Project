import math
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from PIL import Image, ImageTk


def deal_card_one_to_one():
    """
    Affiche les cartes et réalise une distribution 1 à 1
    """
    load_card_images(deck_size)
    for i in range (deck_size):
        gamers[i % gamer_size].append((deck[i], card_images[i]))
    display_cards()


def load_card_images(deck_size):
    """
    Télécharge les cartes
    """
    card_images = []
    for i in range(1, deck_size + 1):
        image = Image.open(f'../images2/{i}.png')
        image = image.resize((110, 165), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        card_images.append(photo)
    return card_images


def display_original_deck(deck):
    """
    Affiche l'ensemble des cartes sur un deck original
    """
    for widget in frame_cards.winfo_children():
        widget.destroy()
    for i, card in enumerate(deck):
        row = i // 13
        column = i % 13
        label = tk.Label(frame_cards, image=card_images[card - 1], bg='#ADD8E6')  # Set card background to light blue
        label.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
        frame_cards.grid_columnconfigure(column, weight=1)


def display_cards():
    """
    Affiche les cartes triées sous le format suivant
    Gamer n°1 -> Cartes
    Gamer n°2 -> Cartes
    ...
    """
    for widget in frame_cards.winfo_children():
        widget.destroy()
    affichage = []
    for no_row in range(gamer_size):
        for no_column in range(len(gamers[no_row])):
            affichage.append(gamers[no_row][no_column][0])
            label = tk.Label(frame_cards, image=gamers[no_row][no_column][1], bg='#ADD8E6')  # Set card background to light blue
            label.grid(row=no_row, column=no_column, padx=5, pady=5, sticky="nsew")
            frame_cards.grid_columnconfigure(no_column, weight=1)
    print(math.log2(len(gamers[no_row])))
    # Calculer le nombre de cartes différentes entre les deux paquets
    nb_cartes_differentes = sum(1 for carte1, carte2 in zip(deck, affichage) if carte1 != carte2)

    # Normaliser la distance entre 0 et 1
    distance_normalisee = nb_cartes_differentes / len(deck)
    print(distance_normalisee)
    print(affichage)


def set_deck_size():
    global deck_size, deck, card_images
    deck_size = simpledialog.askinteger("Nombre de carte par joueurs", "Combien chaque joueur a-t-il de cartes ?", minvalue=2,
                                        maxvalue=52/gamer_size) * gamer_size
    deck = list(range(1, deck_size + 1))
    card_images = load_card_images(deck_size)
    display_original_deck(deck)


def set_gamer_size():
    global gamer_size, gamers
    gamer_size = simpledialog.askinteger("Nombre de joueurs", "Au total, combien de joueurs vont-ils jouer ?", minvalue=2,
                                        maxvalue=52)
    gamers = [[] for _ in range(gamer_size)]


# Fonction pour demander le nombre de cartes
def get_deck_size():
    return simpledialog.askinteger("Taille du deck", "Avec combien de cartes voulez-vous jouer ?", minvalue=2,
                                   maxvalue=52)


window = tk.Tk()
window.title("Méthode de distribution")
window.configure(bg='#2C3E50')

frame_controls = tk.Frame(window, bg='#2C3E50', pady=10)
frame_controls.pack(fill=tk.X)

ttk.Button(frame_controls, text="Nombre de joueurs", command=set_gamer_size).pack(side=tk.LEFT, padx=10)
ttk.Button(frame_controls, text="Nombre de cartes par joueur", command=set_deck_size).pack(side=tk.LEFT, padx=10)
ttk.Button(frame_controls, text="Distribution une à une", command=deal_card_one_to_one).pack(side=tk.LEFT, padx=10)

frame_cards = tk.Frame(window, bg='#ADD8E6')  # Set frame background to light blue
frame_cards.pack(expand=True, fill='both', padx=20, pady=20)

window.mainloop()
