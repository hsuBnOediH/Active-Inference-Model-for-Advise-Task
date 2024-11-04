import sys, os, re, subprocess

subject_list_path = '/mnt/dell_storage/labs/rsmith/lab-members/fli/advise_task/subject_id/advise_subject_IDs_prolific_wo_uncomplete.csv'


results = '/mnt/dell_storage/labs/rsmith/lab-members/fli/advise_task/results/model_comparison/'

if not os.path.exists(results):
    os.makedirs(results)
    print(f"Created results directory {results}")

if not os.path.exists(f"{results}/logs"):
    os.makedirs(f"{results}/logs")
    print(f"Created results-logs directory {results}/logs")

subjects = []
with open(subject_list_path) as infile:
    for line in infile:
        if 'ID' not in line:
            subjects.append(line.strip())

ssub_path = '/mnt/dell_storage/labs/rsmith/lab-members/fli/advise_task/Active-Inference-Model-for-Advise-Task/run_advise_model_comparison.ssub'

for idx_candidate in [1]:
    for subject in subjects:
        stdout_name = f"{results}/logs/{subject}-%J.stdout"
        stderr_name = f"{results}/logs/{subject}-%J.stderr"
        jobname = f'advise-comparison-{subject}-{idx_candidate}'
        os.system(f"sbatch -J {jobname} -o {stdout_name} -e {stderr_name} {ssub_path} {subject} {results} {idx_candidate}")

        print(f"SUBMITTED JOB [{jobname}]")