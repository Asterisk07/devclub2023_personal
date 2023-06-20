import pandas as pd
import nltk

from nltk.corpus import stopwords
# stopwords are commonly used words ignored in preprocessing . 

from nltk.stem import WordNetLemmatizer
# stem : (Verb) reduce word to base or root form. it disregards context
# Lemmaisation considers context too . eg better -> good

import os
# Get the directory path of the current Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script directory
os.chdir(script_dir)
input_file = '../2_processed/out.csv'

# Download NLTK resources (only needed once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load the dataset
df = pd.read_csv(input_file)

# Define stopwords and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Preprocess the title column
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


df['preprocessed_title'] = df['Title'].apply(preprocess_title)
# this applies the function to each entry in Title field in csv file

# or
# df['preprocessed_title'] = df['Title'].apply(lambda x: ' '.join([lemmatizer.lemmatize(word) for word in nltk.word_tokenize(x.lower()) if word.isalpha() and word not in stop_words]))

# Save the preprocessed dataset
df.to_csv(input_file, index=False)
