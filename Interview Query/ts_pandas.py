import re
import pandas as pd
import argparse
import os

# Function to parse transactions from a text file using regex
def parse_boa_transactions(text):
    # Regex to match transactions (date, description, amount)
    transaction_rx = re.compile(r'(\d{2}/\d{2}/\d{2})\s+(.+?)\s+([-]?\d{1,3}(?:,\d{3})*\.\d{2})')
    print(transaction_rx.findall(text))
    return transaction_rx.findall(text)

# Function to load and parse a file, then return a DataFrame
def load_and_parse_file(file_path, account_name):
    with open(file_path, 'r') as f:
        content = f.read()
        transactions = parse_boa_transactions(content)
    
    # Convert to DataFrame
    df = pd.DataFrame(transactions, columns=['Date', 'Description', 'Amount'])
    df['Account'] = account_name
    return df

# Main function to process multiple files and save to a single CSV
def main(files, output_file):
    combined_df = pd.DataFrame(columns=['Date', 'Description', 'Amount', 'Account'])
    
    for file in files:
        account_name = os.path.basename(file).split('.')[0]
        file_df = load_and_parse_file(file, account_name)
        combined_df = pd.concat([combined_df, file_df])
    
    # Remove duplicate checks by grouping on the 'Description' and keeping the first
    combined_df = combined_df.drop_duplicates(subset=['Description'])
    
    # Write to CSV
    combined_df.to_csv(output_file, index=False)
    print(f'Transactions saved to {output_file}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parse BofA statements and output to CSV.")
    parser.add_argument('files', nargs='+', help='List of text files to parse')
    parser.add_argument('--output', help='Output CSV file', default='combined_statements.csv')
    
    args = parser.parse_args()
    main(args.files, args.output)
