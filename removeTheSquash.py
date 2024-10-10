import re

prog_file = open("files/test_prog.txt", "r", encoding="cp1251")

# Separate the header and remove it to append later
prog_header = prog_file.readline()

# Updating the text
prog_content = ""

while True:
    # Removing the quotes
    line = prog_file.readline().replace('"', '')

    # Adding back quotes around each item following proper convention
    time_pattern = r'(\d{2}:\d{2}) '
    age_restriction_pattern = r' \((\d{1,2})\+\)'

    line = re.sub(time_pattern, r'\1 "', line)
    line = re.sub(age_restriction_pattern, r'" (\1+)', line)


    # Appending the updated line
    prog_content += line
    if not line:
        break

# Combining the updated text for final output
prog_output = f'{prog_header}{prog_content}'
print(prog_output)

# Writing output into file
with open("files/output.txt", "w", encoding="cp1251") as output_txt:
    output_txt.write(prog_output)

prog_file.close()
output_txt.close()