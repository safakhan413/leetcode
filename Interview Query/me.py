# Algo:
'''
python parse_boa_statements_me.py account1.txt,account2.txt --output combined_statements.csv    
# first read the two files account1.txt and account2.txt and provide --output in which to write it
python parse_boa_statements.py account1.txt account2.txt --output combined_statements.csv
'''
import argparse
import os
import csv
import shutil

def parse_boa_dump(stringdata):
    # Regex to match transactions (ignoring total lines)
    transaction_rx = re.compile(r'\d\d/\d\d/\d\d.*?\.\d\d', re.IGNORECASE)
    transactions = transaction_rx.findall(stringdata)
    return transactions

def line_to_dict(line):
    # Regex to match transactions (ignoring total lines)
    # transaction_rx = re.compile(r'\d\d/\d\d/\d\d.*?\.\d\d', re.IGNORECASE)
    # transactions = transaction_rx.findall(stringdata)
    trans_rx = re.compile(r'(\d{2}/\d{2}/\d{2})\s(.*)\s(.*\d+)$',  re.IGNORECASE)
    parts = trans_rx.findall(line)
    if parts:
        date, description, amount = parts[0]
        return {'Date': date, 'Description': description.strip(), 'Amount': amount}

class TransformedStatement:
    def __init__(self, dump_file, account = 'unknown'):
        self.dump_path = dump_file
        self.account = account
    def write(self, out_path, columns, mode='a'):
        with open(out_path,mode) as fout:
            writer = csv.DictWriter(fout, columns)
            with open(self.dump_path, 'r') as fin:
                file_data = fin.read()
                parsed_lines = parse_boa_dump(file_data)
                transactions = []
                seen = set()

                for line in parsed_lines:
                    transaction = line_to_dict(line)
                    
                # print(file_data)



 

def main(files, out_path, override_flag, columns):
    basenames = [os.path.basename(os.path.splitext(f)[0]) for f in files]
    src_paths = zip(files, basenames)
    stmts = [TransformedStatement(path, account=act) for path, act in src_paths]
    rowcounts = transform_dump(stmts, columns=columns, out_path=output_file, override_existing_file=override_existing_file)
    return rowcounts
    # print('im basename', src_paths)
    # row_counts = Transforme

if __name__ == '__main__':
    print('hello')
    parser = argparse.ArgumentParser(description="Parse copy/pasted text from BofA statements.")

    parser.add_argument('files', nargs='+', help = 'text files to parse' )
    parser.add_argument('--output', help = 'output file', default = 'combined2.csv')
    parser.add_argument('--override_output', help = 'override existing output', action='store_true')

    args = parser.parse_args()
    print(args)
    files = args.files
    out_path = args.output
    override_flag =args.override_output
    columns = ['Date', 'Descrption', 'Amount', 'Account']

    row_count = main(files, out_path, override_flag, columns=columns)

    print(files)
