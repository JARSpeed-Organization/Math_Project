import matplotlib.pyplot  as plt
import math
import itertools
import random

def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def transform_to_array_of_arrays(arr):
    result = []
    current_group = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            result.append(current_group)
            current_group = [arr[i]]
        else:
            current_group.append(arr[i])

    result.append(current_group)
    return result

def probAmeri(Q, a):
    sm = len(transform_to_array_of_arrays(Q))
    n = len(Q)
    return binomial_coefficient((a + n - sm), n)/a**n

def xAmericain(x):
    return 2**x

def plot_curve(x_values, y_values, xlabel="", ylabel="", title=""):
    plt.plot(x_values, y_values)
    plt.xticks(x_values) 
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()

def createTabForPlot(jeu, nbrDeTest):
    tab = []
    for i in range(nbrDeTest - 1):
        tab.append(probAmeri(jeu, xAmericain(i+1)))
    return tab

def probaAttendu(n):
    return 1/math.factorial(n)


def american_shuffle(deck, num_shuffles):
    for _ in range(num_shuffles):
        new_deck = []
        split_idx = len(deck) // 2
        for i in range(split_idx):
            print("test")
            new_deck.append(deck[i + split_idx])
            new_deck.append(deck[i])
        deck = new_deck
    return deck
 

plot_curve(list(range(1, 11)), createTabForPlot([2,3,4,5,6,7,8,9,10], 11), "Nombre de 2-mélange", "Probabilité", "Probabilité d'obtenir un ordre Q (3,8,5,2,4,6,7,A,Q,J,K,9,10)")
print(probAmeri([3,8,5,2,4,6,7,1,12,11,13,9,10],xAmericain(3)))
