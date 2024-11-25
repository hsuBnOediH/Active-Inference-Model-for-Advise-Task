import os
import re
import argparse
from collections import defaultdict

def find_incomplete_runs(num_indices):
    # Define the directory containing the files
    directory_path = '/mnt/dell_storage/labs/rsmith/lab-members/fli/advise_task/results/balanced_AI/'

    # Pattern to match filenames like "advice_task_model_identification_[uuid]_[idx].csv"
    pattern = re.compile(r'advice_task_model_identification_([a-f0-9\-]+)_(\d+)\.csv')

    # Dictionary to store idx values for each uuid
    uuid_idx_map = defaultdict(list)

    # Iterate over each file in the directory
    for filename in os.listdir(directory_path):
        match = pattern.match(filename)
        if match:
            uuid, idx = match.groups()
            uuid_idx_map[uuid].append(int(idx))  # Convert idx to integer for easier sorting

    # Track counts of matching and non-matching UUIDs
    match_count = 0
    unmatch_count = 0

    # Print UUIDs and indices only if the length of indices doesn't match the argument
    for uuid, idx_list in uuid_idx_map.items():
        if len(idx_list) == num_indices:
            match_count += 1
        else:
            unmatch_count += 1
            print(f"UUID: {uuid}, Indices run: {sorted(idx_list)}")

    # Summary of match and unmatch counts
    print("\nSummary:")
    print(f"Total UUIDs with matching indices count ({num_indices}): {match_count}")
    print(f"Total UUIDs with non-matching indices count: {unmatch_count}")

# Set up argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find incomplete model runs.")
    parser.add_argument("num_indices", type=int, help="Expected number of indices for each UUID")
    args = parser.parse_args()

    # Run the function with the provided argument
    find_incomplete_runs(args.num_indices)