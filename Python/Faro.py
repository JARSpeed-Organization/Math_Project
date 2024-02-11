import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from PIL import Image, ImageTk


def faro_out_shuffle(deck):
    half = len(deck) // 2
    return [val for pair in zip(deck[:half], deck[half:]) for val in pair]


def faro_in_shuffle(deck):
    half = len(deck) // 2
    return [val for pair in zip(deck[half:], deck[:half]) for val in pair]


def load_card_images(deck_size):
    card_images = []
    for i in range(1, deck_size + 1):
        image = Image.open(f'../images2/{i}.png')
        image = image.resize((110, 165), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        card_images.append(photo)
    return card_images


def display_cards(deck):
    for widget in frame_cards.winfo_children():
        widget.destroy()
    for i, card in enumerate(deck):
        row = i // 13
        column = i % 13
        label = tk.Label(frame_cards, image=card_images[card - 1], bg='#ADD8E6')  # Set card background to light blue
        label.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
        frame_cards.grid_columnconfigure(column, weight=1)


def set_deck_size():
    global deck_size, deck, card_images
    deck_size = simpledialog.askinteger("Taille du deck", "Avec combien de cartes voulez-vous jouer ?", minvalue=2,
                                        maxvalue=52)
    deck = list(range(1, deck_size + 1))
    card_images = load_card_images(deck_size)
    display_cards(deck)


def shuffle_and_display(shuffle_type):
    global deck
    if shuffle_type == 'in':
        deck = faro_in_shuffle(deck)
    else:
        deck = faro_out_shuffle(deck)
    display_cards(deck)


# Fonction pour demander le nombre de cartes
def get_deck_size():
    return simpledialog.askinteger("Taille du deck", "Avec combien de cartes voulez-vous jouer ?", minvalue=2,
                                   maxvalue=52)


def calculate_shuffles(deck_size):
    # Cas spécifiques donnés dans l'article
    specific_cases = {
        2: 1, 4: 2, 6: 4, 8: 3, 10: 6, 12: 10, 14: 12, 16: 4, 18: 8,
        20: 18, 22: 6, 24: 11, 26: 20, 28: 18, 30: 28, 32: 5, 34: 10,
        36: 12, 38: 36, 40: 12, 42: 20, 44: 14, 46: 12, 48: 23, 50: 21, 52: 8
    }

    # Retourne le résultat directement si dans les cas spécifiques
    if deck_size in specific_cases:
        return specific_cases[deck_size]

    # Calcul pour les nombres de cartes non spécifiés directement
    if deck_size % 2 == 0:  # Si le nombre de cartes est pair
        k = 1
        while (2 ** k - 1) % (deck_size - 1) != 0:
            k += 1
        return k

    return "Non défini pour ce nombre de cartes"


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

frame_cards = tk.Frame(window, bg='#ADD8E6')  # Set frame background to light blue
frame_cards.pack(expand=True, fill='both', padx=20, pady=20)

window.mainloop()