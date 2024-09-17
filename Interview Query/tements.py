import re
import csv
import shutil
import os
import argparse

# Function to validate whether a line contains a date and follows the correct format
def validate_line(l):
    return l[0].isnumeric() and '/' in l.split()[0]

# Function to extract line information into a dictionary with Date, Description, and Amount
def line_to_dict(line):
    parts = re.findall(r'(\d+/\d+/\d+)\s(.*)\s(.*\d+)$', line)
    if parts:
        date, description, amount = parts[0]
        return {'Date': date, 'Description': description.strip(), 'Amount': amount}

# Function to parse text and extract transactions using regex
def parse_boa_dump(stringdata):
    # Regex to match transactions (ignoring total lines)
    transaction_rx = re.compile(r'\d\d/\d\d/\d\d.*?\.\d\d', re.IGNORECASE)
    transactions = transaction_rx.findall(stringdata)
    return transactions

# Class representing a transformed statement
class TransformedStatement:

    def __init__(self, dump_path, account='unknown'):
        self.dump_path = dump_path
        self.account = account

    # Writes parsed transactions to a CSV
    def write(self, out_path, columns, mode='a'):
        with open(out_path, mode) as fout:
            writer = csv.DictWriter(fout, columns)

            with open(self.dump_path, 'r') as fin:
                file_data = fin.read()
                parsed_lines = parse_boa_dump(file_data)
                transactions = []

                # Extract transactions and avoid duplicates for checks
                seen_checks = set()
                for line in parsed_lines:
                    transaction = line_to_dict(line)
                    if 'Check' in transaction['Description']:
                        # Ensure check is not duplicated
                        if transaction['Description'] not in seen_checks:
                            seen_checks.add(transaction['Description'])
                            transaction['Account'] = self.account
                            transactions.append(transaction)
                    else:
                        transaction['Account'] = self.account
                        transactions.append(transaction)

                writer.writerows(transactions)
                return len(transactions)

# Function to manage multiple statements and output combined results into one CSV

# shutil.move() is a function in Python's shutil module that allows you to move a file or directory from one location to another. It is commonly used for file or directory management tasks in Python, such as relocating files, renaming them, or transferring them across directories or even different file systems.

# Here’s a breakdown of how shutil.move() works:

# Syntax:
# python
# Copy code
# shutil.move(src, dst)
# src: This is the path to the source file or directory you want to move.
# dst: This is the path to the destination where you want to move the file or directory. It can be a file name (to rename the file) or a director
def transform_dump(transformed_statements, columns=None, out_path='transformed_statements.csv', override_existing_file=False):
    out_path = os.path.abspath(out_path)
    exists = os.path.exists(out_path)
    if not override_existing_file and exists:
        raise Exception(f'File exists: {out_path}')

    out_path_temp = out_path + '.temp'
    with open(out_path_temp, 'w') as fout:
        writer = csv.DictWriter(fout, columns)
        writer.writeheader()

    rowcounts = []
    for stmt in transformed_statements:
        rowcounts.append(stmt.write(out_path_temp, columns, mode='a'))

    shutil.move(out_path_temp, out_path)
    return rowcounts

# Main function to handle input files and generate output


#     3. os.path.splitext(f)[0]
# Purpose: This part removes the file extension from the filename. The function os.path.splitext() splits the filename into two parts:
# The first part is the file name without the extension.
# The second part is the file extension.
# Example: If f = "/home/user/file.txt", then os.path.splitext(f) returns a tuple ('/home/user/file', '.txt'). The [0] index retrieves the first part ('/home/user/file'), which is the file path without the extension.
# 4. os.path.basename(...)
# Purpose: This function takes a full path and returns only the last part, which is the actual file name without the directories.
# Example: If the input is '/home/user/file', then os.path.basename() will return 'file'. This removes any directory structure, leaving just the base file name.
# 5. [os.path.basename(os.path.splitext(f)[0]) for f in files]
# Purpose: This is a list comprehension that applies the steps above to each file path in files. It:
# Takes each file path (f) from the files list.
# Strips the file extension using os.path.splitext(f)[0].
# Extracts just the file name (without directories) using os.path.basename().
# Collects the resulting base name into a list.
# Example Breakdown:
# Let’s assume files = ["/home/user/file1.txt", "/var/log/file2.log", "file3.py"].

# For the first file "/home/user/file1.txt":

# os.path.splitext(f)[0] will return "/home/user/file1".
# os.path.basename("/home/user/file1") will return "file1".
# For the second file "/var/log/file2.log":

# os.path.splitext(f)[0] will return "/var/log/file2".
# os.path.basename("/var/log/file2") will return "file2".
# For the third file "file3.py":

# os.path.splitext(f)[0] will return "file3".
# os.path.basename("file3") will return "file3".

def main(files, output_file, columns=None, override_existing_file=True):

    basenames = [os.path.basename(os.path.splitext(f)[0]) for f in files]
    source_paths = zip(files, basenames)
    stmts = [TransformedStatement(path, account=act) for path, act in source_paths]
    rowcounts = transform_dump(stmts, columns=columns, out_path=output_file, override_existing_file=override_existing_file)
    return rowcounts

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parse copy/pasted text from BofA statements.")
    parser.add_argument('file', nargs='+', help='Paths to the text files (separated by spaces).')
    parser.add_argument('--output', help='Output path', default='combined_statements.csv')
    parser.add_argument('--override_output', help='Override existing output file if it exists', action='store_true')

    args = parser.parse_args()
    files = args.file
    out_path = args.output
    override_existing_file = args.override_output
    columns = ['Date', 'Description', 'Amount', 'Account']

    rowcounts = main(files, out_path, columns=columns, override_existing_file=override_existing_file)

    if not rowcounts:
        print(f'No rows transformed to file {out_path}')
    else:
        # eg 7 rows from 2 files transformed to file combined_statements.csv
        print(f'{sum(rowcounts)} rows from {len(rowcounts)} files transformed to file {out_path}')
