import re
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()
prog_filename = str(args.filename)

prog_file = open(prog_filename, "r", encoding="cp1251")

# Separate the header to append later
prog_header = prog_file.readline()

# Setting up regular expressions
time_pattern = r'(\d{2}:\d{2}) '
age_restriction_pattern = r' \((\d{1,2})\+\)'
date_pattern = r'\d{2}/\d{2}/\d{4}'

prog_content = ""

for line in prog_file:
    # Removing the quotes
    line = line.replace('"', '')

    # Check if the line contains date
    if re.search(date_pattern, line):
        line = f'\n{line}\n'

    # Check if the line is a TV guide item and place quotes accordingly
    elif re.search(time_pattern, line):
        line = re.sub(time_pattern, r'\1 "', line)

        # The item contains age restriction
        if re.search(age_restriction_pattern, line):
            line = re.sub(age_restriction_pattern, r'" (\1+)', line)
        else:
            line = line.strip("\n") + '"\n'

    # The line is empty or contains unnecessary data
    else:
        line = ""

    # Appending the updated line
    prog_content += line

# Combining the updated text for final output
prog_output = f'{prog_header}{prog_content}'
print("Successfully written!")

# Writing output into file
if not os.path.exists('output'):
    os.mkdir('output')
with open(f"output/{prog_filename}", "w", encoding="cp1251") as output_txt:
    output_txt.write(prog_output)

prog_file.close()
output_txt.close()