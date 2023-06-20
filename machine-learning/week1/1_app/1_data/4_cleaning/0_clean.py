import csv
import os

# Get the directory path of the current Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script directory
os.chdir(script_dir)

module_name = '1_duplication'
function_name = 'remove_consecutive_duplicates'

# Define the input and output file paths
input_file = '../1_raw/try.csv'
output_file = '../2_processed/out.csv'

module = __import__(module_name)
remove_consecutive_duplicates = getattr(module, function_name)


# puzzle = __import__('puzzler')

# import puzzler as puzzle
# from 1_duplication import remove_consecutive_duplicates

# Define your preprocessing function here
def preprocess_data(input_file, output_file):
    pass
    # Your preprocessing code goes here



# Remove consecutive duplicates
remove_consecutive_duplicates(input_file, output_file)

# Preprocess the data
# preprocess_data(output_file, output_file)

print("finished cleaning successfully")
