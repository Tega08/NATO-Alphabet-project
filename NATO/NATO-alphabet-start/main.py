import pandas

nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in nato_file.iterrows()}


def nato_words():
    word = input("Enter a word: ").upper()
    try:
        nato_word = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the english alphabet.")
        nato_words()
    else:
        print(nato_word)


nato_words()


