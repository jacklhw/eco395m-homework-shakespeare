import csv
import os
import re

INPUT_DIR = os.path.join("data", "shakespeare")
STOPWORDS_PATH = os.path.join(INPUT_DIR, "stopwords.txt")
SHAKESPEARE_PATH = os.path.join(INPUT_DIR, "shakespeare.txt")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "shakespeare_report.csv")

NUM_LINES_TO_SKIP = 246
LAST_LINE_START = "End of this Etext"


def load_stopwords():
    """Load the stopwords from the file and return a set of the cleaned stopwords."""

    stopwords = set(line.strip() for line in open(STOPWORDS_PATH,"r",encoding='cp437'))
    print(type(stopwords))


    # fill this in

    return stopwords


def load_shakespeare_lines():
    "Loads every line in the dataset that was written by Shakespeare as a list of strings."

    shakespeare_lines = []

    # fill this in
    with open(SHAKESPEARE_PATH, "r") as file:
        shakespeare_lines = file.readlines()[246:-7]
    result = re.sub('<<(\n|.)+?>>',"",str(shakespeare_lines))

#accoring to geeksforgeeks.org
    def Convert(string):
        li = list(string.split(" "))
        return li


    shakespeare_lines = Convert(result)
    return shakespeare_lines


def get_shakespeare_words(shakespeare_lines):
    """Takes the lines and makes a list of lowercase words."""

    # fill this in

    words = []
    for i in shakespeare_lines:
        words.append(i.lower())
    clean_words = re.sub('/.*n', ' ', str(words))
    clean_text = re.sub('[^A-Za-z/s]', ' ', str(clean_words))
    text_with_only_spaces = re.sub("/s+", " ", str(clean_text))

    words = text_with_only_spaces
    #accoring to geeksforgeeks.org
    def Convert(string):
        li = list(string.split(" "))
        return li
    words = Convert(words)
    return words


def count_words(words, stopwords):
    """Counts the words that are not stopwords.
    returns a dictionary with words as keys and values."""

    word_counts = dict()

    # fill this in
    word_counts = dict()
    real_words = [item for item in words if item not in stopwords]
    
    def char_count(str_):

            char_counts = {}

            for char_ in str_:

                if char_ in char_counts:
                    char_counts[char_] += 1
                else:
                    char_counts[char_] = 1

            return char_counts
    result = char_count(real_words)
    word_counts = result
    return word_counts


def sort_word_counts(word_counts):
    """Takes a dictionary or word counts.
    Returns a list of (word, count) tuples that are sorted by count in descending order."""

    # fill this in
    sorted_word_counts = sorted(word_counts.items(), key=lambda e: e[1], reverse=True)

    return sorted_word_counts


def write_word_counts(sorted_word_counts, path):
    """Takes a list of (word, count) tuples and writes them to a CSV."""

       # fill this in

    with open(OUTPUT_PATH, "w+") as shakespeare_report:

        csv_writer = csv.writer(shakespeare_report)

        csv_writer.writerow(["word", "count"])
        for row in sorted_word_counts:
            csv_writer.writerow(row)

if __name__ == "__main__":

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    stopwords = load_stopwords()

    shakespeare_lines = load_shakespeare_lines()
    shakespeare_words = get_shakespeare_words(shakespeare_lines)

    word_counts = count_words(shakespeare_words, stopwords)
    word_counts_sorted = sort_word_counts(word_counts)

    write_word_counts(word_counts_sorted, OUTPUT_PATH)
