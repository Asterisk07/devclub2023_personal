import csv
import os
# Get the directory path of the current Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script directory
os.chdir(script_dir)
input_file = '../1_raw/try.csv'
# input_file = '../1_raw/big.csv'
output_file = '../2_processed/out.csv'

# Read the input CSV file with the specified encoding
with open(input_file, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    # Perform data processing
    processed_data = []
    for row in reader:
        # Extract first and second words from the title field
        title_words = row['Title'].split()
        if len(title_words) >= 2:
            clean_title = {'word1': title_words[0], 'word2': title_words[1]}
        else:
            clean_title = {}
        # Add the clean_title field to the row dictionary
        row['clean_title'] = clean_title
        processed_data.append(row)

# Write the processed data to the output CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    fieldnames = processed_data[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(processed_data)

print("Data processing and writing complete.")
