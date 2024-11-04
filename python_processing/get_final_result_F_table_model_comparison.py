import os
import csv
import re

# Define path to your files
path = '/mnt/dell_storage/labs/rsmith/lab-members/fli/advise_task/results/model_comparison/'

# Initialize the dictionary to store UUIDs and their F values for 10 indexes
uuid_dict = {}

# Define a regex pattern to match file names and capture the UUID and index
pattern = re.compile(r"advice_task_model_comparsion_([a-fA-F0-9\-]+)_(\d+)\.csv")

# Iterate over all files in the directory
for file_name in os.listdir(path):
    match = pattern.match(file_name)
    if match:
        # Extract UUID and index from the file name
        uuid = match.group(1)
        idx = int(match.group(2)) - 1
        
        # Ensure the UUID is in the dictionary with a 10-element array initialized to 0
        if uuid not in uuid_dict:
            uuid_dict[uuid] = [0] * 10

        # Read the file
        file_path = os.path.join(path, file_name)
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

            # Extract the F value from the last column of the second row (index 1)
            f_value = float(rows[1][-1])

            # Assign the F value to the correct index in the dictionary
            uuid_dict[uuid][idx] = f_value

# Create the output CSV file
output_csv_path = os.path.join(path, "final_res/output_f_values_comparison.csv")
with open(output_csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write header
    header = ['uuid'] + [f"idx_{i+1}" for i in range(10)]
    writer.writerow(header)
    
    # Write UUIDs and their values, sorted by UUID
    for uuid in sorted(uuid_dict.keys()):
        writer.writerow([uuid] + uuid_dict[uuid])

print(f"Output saved to {output_csv_path}")