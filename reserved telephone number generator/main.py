import os
import time


def generate_phone_numbers(area_codes):
    with open('numbers.txt', 'w') as numbers_file:
        for code in area_codes:
            for number in range(10000000):  # 7-digit numbers from 0000000 to 9999999
                phone_number = f"{code}{number:07d}\n"  # Pad the number with zeros
                numbers_file.write(phone_number)


def main():
    start_time = time.time()

    area_codes = []
    with open('codes.txt', 'r') as codes_file:
        for line in codes_file:
            area_codes.append(line.strip())

    generate_phone_numbers(area_codes)

    line_count = 0
    with open('numbers.txt', 'r') as numbers_file:
        for _ in numbers_file:
            line_count += 1

    file_size_bytes = os.path.getsize('numbers.txt')
    file_size_gigabytes = file_size_bytes / (1024 ** 3)  # Convert bytes to GB

    formatted_line_count = f"{line_count:,}"
    formatted_file_size = f"{file_size_gigabytes:.1f}GB"

    print(f"Total number of phone numbers generated: {formatted_line_count}")
    print(f"Size of 'numbers.txt': {formatted_file_size}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes, seconds = divmod(elapsed_time, 60)
    print(f"Time taken: {int(minutes)} minutes and {int(seconds)} seconds")


if __name__ == '__main__':
    main()
