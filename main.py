import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(new_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs
word = input("enter a word: ").upper()
result = [new_dict[n] for n in word]
print(result)