import os

import re

import argparse

from collections import defaultdict



def find_incomplete_runs(num_indices, run_idx):

    # Define the directory containing the files

    parsent_folde_path = '/mnt/dell_storage/labs/rsmith/lab-members/fli/advise_task/ai_results/'

    # list all the folders in the parent folder

    print(f"Scanning parent folder: {parsent_folde_path}")

    subfolders = os.listdir(parsent_folde_path)

    # sort and get the tartget folder by run_idx

    subfolders.sort()

    print(f"Subfolders: {subfolders}")

    target_folder = parsent_folde_path + subfolders[-run_idx] + '/logs'



    # Dictionary to store idx values for each uuid

    uuid_idx_map = defaultdict(list)



    # Iterate over each file in the directory

    for filename in os.listdir(target_folder):

        # split the filename by '-'

        filename_parts = filename.split('-')

        uuid = filename_parts[0]

        model_idx = filename_parts[1]

        task_id = filename_parts[2]

       



        uuid_idx_map[uuid].append(int(model_idx))  # Convert idx to integer for easier sorting



    # Track counts of matching and non-matching UUIDs

    match_count = [0] * num_indices

    unmatch_count = [0] * num_indices



    for i in range(1, num_indices + 1):

        print("*"*20)

        print(f"Model index {i}")

        # Check each UUID for missing indices

        for uuid, idx_list in uuid_idx_map.items():

            if i in idx_list:

                match_count[i - 1] += 1

            else:

                unmatch_count[i - 1] += 1

       

        print(f"Match count: {match_count[i - 1]}")

        print(f"Unmatch count: {unmatch_count[i - 1]}")

# Set up argument parsing

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Find incomplete model runs.")

    parser.add_argument("num_indices", type=int, help="Expected number of indices for each UUID")

    parser.add_argument("run_idx", type=int, help="Index of the run folder to check",default=1)



    args = parser.parse_args()

   

    # Run the function with the provided argument

    find_incomplete_runs(args.num_indices, args.run_idx)