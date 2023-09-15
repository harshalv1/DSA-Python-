import os

# Specify the folder path
folder_path = '/Users/harshalrathod/Downloads/nifty 50 (2000-2021)'

# List all files in the folder
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Print the list of file names
for file_name in file_names:
    root, ext = os.path.splitext(file_name)
    new_file_name = root + '.NS'
    print(new_file_name)

