import nltk
import pyttsx3

# Download the WordNet data if not already downloaded
nltk.download("wordnet")

from nltk.corpus import wordnet


def get_word_meaning(word):
    meanings = wordnet.synsets(word)

    if meanings:
        meaning_str = ""
        for synset in meanings:
            meaning_str += f"{synset.definition()}\n"
        return meaning_str
    else:
        return "Word not found in the dictionary."


def get_word_explanation(word):
    meanings = wordnet.synsets(word)

    if meanings:
        return meanings[0].definition()
    else:
        return "Word not found in the dictionary."


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    while True:
        choice = input("Enter '1' for word meaning or '2' for one-line explanation (Press 'q' to quit): ")

        if choice == 'q':
            break

        word = input("Enter a word: ")

        if choice == '1':
            meaning = get_word_meaning(word)
            print(meaning)
        elif choice == '2':
            explanation = get_word_explanation(word)
            print(explanation)

        listen_choice = input("Do you want to listen? (y/n): ")
        if listen_choice.lower() == 'y':
            speak(meaning if choice == '1' else explanation)
