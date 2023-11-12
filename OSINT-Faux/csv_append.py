import csv
import os

def process_csv(file_path, data_set, encoding):
    try:
        with open(file_path, mode='r', encoding=encoding) as file:
            reader = csv.reader(file)
            for _ in range(7):  # Skip the first 7 rows
                next(reader, None)
            
            for row in reader:
                if len(row) > 5:  # Ensure row has at least F column
                    # Adding individual entries from columns B and F
                    data_set.add(row[1].strip())
                    data_set.add(row[5].strip())
    except UnicodeDecodeError:
        if encoding == 'utf-8':
            process_csv(file_path, data_set, 'iso-8859-1')
        else:
            print(f"Failed to decode file {file_path} with both utf-8 and iso-8859-1 encodings.")

def main(directory, output_file):
    all_data = set()

    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            process_csv(file_path, all_data, 'utf-8')

    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name'])  # Header
        for item in all_data:
            writer.writerow([item])

if __name__ == "__main__":
    directory_path = 'Scottish_Names'
    output_path = 'names_no_duplicates.csv'
    main(directory_path, output_path)
