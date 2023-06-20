# note: sort files on basis of id before doing this
# this is for men and women file

import csv
import os
# Get the directory path of the current Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script directory
os.chdir(script_dir)
def remove_consecutive_duplicates(input_file, output_file):
    last_value = None

    with open(input_file, 'r',encoding='utf-8') as in_file, open(output_file, 'w', newline='',encoding='utf-8') as out_file:
        reader = csv.reader(in_file)
        writer = csv.writer(out_file)

        for row in reader:
            current_value = row[0]  # Assuming the first column is at index 0

            if current_value != last_value:
                writer.writerow(row)
                last_value = current_value
    print("successfully removed duplicates")

# Example usage
input_file = '../1_raw/try.csv'
output_file = '../2_processed/out.csv'

if __name__=='__main__':
    remove_consecutive_duplicates(input_file, output_file)

    
