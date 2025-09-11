
import tkinter as tk
import random
import pyjokes

from tkinter import ttk



dog_jokes = [
    "Dogs can’t operate MRI machines, but they’re great at running Lab reports",
    "Dogs are terrible with boundaries—instead of standing up for themselves, they just roll over.",
    "A three-legged dog limps into a saloon and yells, “Listen up! I’m looking for the man who shot my paw!",
    "If you want your dog to stop digging up your garden, all you have to do is take away his shovel",
    "Heaven forbid you forget to feed your dog, he’ll hound you about it all day.",
    "If you want your dog to stop digging up your garden, all you have to do is take away his shovel."

]

cat_jokes = [
    "What do you call a stylish cat? A dandy lion",
    "What's a cat's favorite color? Purr-ple.",
    "What do you call a tiger that likes pickles? A sour puss.",
    "Why don't cats shop in stores? They prefer cat-alogs.",
    "What is a cat's favorite song? “Three Blind Mice.”",
    "What do cats eat for breakfast? Mice Krispies.",
    "Why don't leopards play hide-and-go-seek? They're always spotted."

]


#function to Choose random Joke from list
def grab_joke():

    try:
        joke_type = entry.get()
        print(joke_type)

        if joke_type == 'Programmer':
            random_choice = pyjokes.get_joke()
            entry.delete(0, tk.END)
            entry.insert(0, random_choice)

        elif joke_type == 'Short but Sweet':
            random_choice = random.choice(dog_jokes)
            entry.delete(0, tk.END)
            entry.insert(0, random_choice)

        elif joke_type == 'Woof Woof':
            random_choice = random.choice(dog_jokes)
            entry.delete(0, tk.END)
            entry.insert(0, random_choice)

        elif joke_type == 'Boots n Cats':
            random_choice = random.choice(cat_jokes)
            print(random_choice)
            entry.delete(0, tk.END)
            entry.insert(0, random_choice)

        else:
            random_choice = "null"

    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")





def clear_joke():
    entry.delete(0, tk.END)


#buttons to indicate which kind of joke to tell
# button the generate joke
# screen to display joke

def click_button(value):

    entry.delete(0, tk.END)
    entry.insert(0, str(value))

root = tk.Tk()
root.title("Joke Generator")

entry = tk.Entry(root, width=100, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)


buttons = [
('Programmer', 1, 1), ('Woof Woof', 2, 1), ('Short but Sweet', 3, 1), ('Boots n Cats', 4, 1),
]

for (text, row, column) in buttons:
    button = tk.Button(
        root,
        activebackground="yellow",
        activeforeground="blue",
        padx=0,
        pady=2,
        text=text,
        bd=3,
        width=12,
        height=3,
        command=lambda t=text: click_button(t))
    button.grid(row=row, column=column)

    # Special case for the equals button
    generate_joke_button = tk.Button(root, text="Generate Joke", width=12, height=2, command=grab_joke)
    generate_joke_button.grid(row=4, column=2)

    clear_button = tk.Button(root, text="Its not Funny anymore", width=19, height=2, command=clear_joke)
    clear_button.grid(row=4, column=3)






root.mainloop()




#dad_jokes
#knock_knock
#one_liners
#short jokes
#dog_jokes

