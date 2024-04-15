import tkinter as tk
import random

def check_guess():
    global kata, guesses, turns, label_word, label_turns, label_result
    
    guess = entry_guess.get()
    entry_guess.delete(0, tk.END)
    
    if guess not in guesses:
        guesses += guess
        if guess not in kata:
            turns -= 1
    
    hidden_word = ""
    for char in kata:
        if char in guesses:
            hidden_word += char + " "
        else:
            hidden_word += "_ "
    
    label_word.config(text=hidden_word)
    label_turns.config(text="Turns left: " + str(turns))
    
    if set(kata).issubset(set(guesses)):
        label_result.config(text="You Win! The word is: " + kata)
        entry_guess.config(state=tk.DISABLED)
    elif turns == 0:
        label_result.config(text="You Lose! The word was: " + kata)
        entry_guess.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Guess the Word")
root.geometry("500x500")


label_name = tk.Label(root, text="Siapa nama anda?")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

def start_game():
    global nama, kata, guesses, turns, label_word, label_turns, label_result, entry_guess
    
    nama = entry_name.get()
    entry_name.config(state=tk.DISABLED)
    button_start.config(state=tk.DISABLED)
    
    kata = random.choice(katakata)
    guesses = ""
    turns = 12
    
    hidden_word = "_ " * len(kata)
    label_word = tk.Label(root, text=hidden_word)
    label_word.pack()
    
    label_turns = tk.Label(root, text="Turns left: " + str(turns))
    label_turns.pack()
    
    label_result = tk.Label(root)
    label_result.pack()
    
    label_guess = tk.Label(root, text="Guess a character:")
    label_guess.pack()
    
    entry_guess = tk.Entry(root)
    entry_guess.pack()
    
    button_guess = tk.Button(root, text="Guess", command=check_guess)
    button_guess.pack()

button_start = tk.Button(root, text="Start Game", command=start_game)
button_start.pack()

katakata = ["macan",'harimau',"singa","kancil","kuda","monyet","jerapah","naga","buaya","menjangan","rusa","simpanse","sapi"]

root.mainloop()