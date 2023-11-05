import tkinter as tk
from tkinter import messagebox
import requests


def get_pokemon_names():
    url = "https://pokeapi.co/api/v2/pokemon?limit=100"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for pokemon in data['results']:
            name = pokemon['name']
            listbox.insert(tk.END, name)
    else:
        print("API isteği başarısız.")

def get_pokemon_info():

    pokemon_name = entry.get()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()

        info_label.config(text=f"Pokemon Name: {pokemon_data['name']}\nID: {pokemon_data['id']}\nTypes: {', '.join([t['type']['name'] for t in pokemon_data['types']])}\nAbility: {', '.join([a['ability']['name'] for a in pokemon_data['abilities']])}\nWeight: {pokemon_data['weight']}\nHeight: {pokemon_data['height']}")
    else:
        messagebox.showerror("Error", f"{pokemon_name} adında bir Pokemon bulunamadı veya istek başarısız oldu. Durum kodu: {response.status_code}")

root = tk.Tk()
root.title("Pokemon Bilgi Arayüzü")
root.geometry("400x400")

label = tk.Label(root, text="Pokemon Name:")
label.pack()
entry = tk.Entry(root)
entry.pack()

info_label = tk.Label(root, text="", justify="left")
info_label.pack()

get_info_button = tk.Button(root, text="Get info", command=get_pokemon_info)
get_info_button.pack()


listbox = tk.Listbox(root)
listbox.pack()

fetch_button = tk.Button(root, text="Get Pokemon Names", command=get_pokemon_names)
fetch_button.pack()

root.mainloop()
