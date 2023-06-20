import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('wordnet')
stop_words = set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()


def preprocess_title(title):
    # print(title)
    # print(type(title))
    # raise ZeroDivisionError
    tokens = nltk.word_tokenize(title.lower())  # Tokenize the text and convert to lowercase
    
    lemmatized_tokens = []
    for word in tokens:
        if word.isalpha() and word not in stop_words:  # Filter out non-alphabetic words and stopwords
            lemmatized_word = lemmatizer.lemmatize(word)  # Lemmatize each word
            lemmatized_tokens.append(lemmatized_word)
    
    preprocessed_title = ' '.join(lemmatized_tokens)  # Join the lemmatized tokens back into a single string
    return preprocessed_title


while True:
    sentence = input("Enter a sentence: ")

    if sentence == "":
        break

    # # Tokenize the sentence into words
    # words = nltk.word_tokenize(sentence)

    # # Lemmatize each word
    # lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

    # # Join the lemmatized words back into a sentence
    # lemmatized_sentence = " ".join(lemmatized_words)

    print("Lemmatized sentence:", preprocess_title(sentence))
