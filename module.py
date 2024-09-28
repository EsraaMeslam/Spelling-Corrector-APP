
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')


class CheckerModule:
    def __init__(self):
        self.correct = TextBlob("")

    def correct_spell(self, text):
        words = word_tokenize(text)
        corrected_words = []
        incorrect_words = {}

        for word in words:
            corrected_word = str(TextBlob(word).correct())
            if word != corrected_word:
                incorrect_words[word] = corrected_word
            corrected_words.append(corrected_word)

        corrected_text = " ".join(corrected_words)
        return corrected_text, incorrect_words


if __name__ == "__main__":
    obj = CheckerModule()
    msg = "i am a cmputer scinece studnt"
    corrected_text, incorrect_words = obj.correct_spell(msg)
    print("Corrected Text:", corrected_text)
    print("Incorrect Words:", incorrect_words)
