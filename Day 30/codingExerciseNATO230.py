"""NATO handling Errors"""
import pandas

dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
print(dataframe)
data_dict = {word["letter"]:word["code"] for (_, word) in dataframe.iterrows()}
print(data_dict)

def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        phonetic_list = [data_dict[letter] for letter in user_input]
    except KeyError as e:
        print(f"{e} is not a word")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()



