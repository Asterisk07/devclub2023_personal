import os

def create_directories():
    # Create the main app directory
    os.makedirs('1_app')

    # Create data directory and subdirectories
    os.makedirs('1_app/1.1_data/1.1.1_raw')
    os.makedirs('1_app/1.1_data/1.1.2_processed')
    os.makedirs('1_app/1.1_data/1.1.3_models')

    # Create src directory and subdirectories
    os.makedirs('1_app/1.2_src/1.2.1_utils')
    os.makedirs('1_app/1.2_src/1.2.2_models')

    # Create tests directory
    os.makedirs('1_app/1.3_tests')

    # Create config directory
    os.makedirs('1_app/1.4_config')

    # Create docs directory
    os.makedirs('1_app/1.5_docs')

def create_files():
    # Create train.py file
    with open('1_app/1.2_src/1.2.3_train.py', 'w') as file:
        pass

    # Create predict.py file
    with open('1_app/1.2_src/1.2.4_predict.py', 'w') as file:
        pass

    # Create requirements.txt file
    with open('1_app/1.6_requirements.txt', 'w') as file:
        pass

    # Create README.md file
    with open('1_app/1.7_README.md', 'w') as file:
        pass

# Call the functions to create directories and files
create_directories()
create_files()
