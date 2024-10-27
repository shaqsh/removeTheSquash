import re
import os

if not os.path.exists('input'):
    os.mkdir('input')

input_dir = 'input'
file_list = os.listdir(input_dir)

if not file_list:
    print("Директория 'input' пуста\nПереместите нужные файлы в директорию 'input'")
else:
    for file in file_list:
        with open(f'input/{file}', "r", encoding="cp1251") as prog_file:
            print(f'Открываю "{file}"...')

            # Separate the header to append later
            prog_header = prog_file.readline()

            # Check is guide is for the ОТР channel and change the header accordingly
            if re.search("ОТР", file):
                prog_header = re.sub("Кубань 24", "Кубань 24 ОТР", prog_header)

            # Setting up regular expressions
            time_pattern = r'(\d{2}:\d{2}) '
            age_restriction_pattern = r' \((\d{1,2})\+\)'
            date_pattern = r'\d{2}/\d{2}/\d{4}'

            prog_content = ""

            for line in prog_file:
                # Removing the quotes
                line = line.replace('"', '')

                # The line contains date
                if re.search(date_pattern, line):
                    line = f'\n{line}\n'

                # Placing back quotes
                # The line is a TV guide item
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

            # Writing output into file
            if not os.path.exists('output'):
                os.mkdir('output')
            with open(f"output/{file}", "w", encoding="cp1251") as output_txt:
                output_txt.write(prog_output)
                print(f'» » »\nФайл "{file}" записан в директорию "output"\n')