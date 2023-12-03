import os
import time

def count_lines(file_path):
    """Counts the number of lines in a file."""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return sum(1 for _ in file)

def split_file(file_path, part1_path, part2_path):
    """Splits a file into two parts at the midpoint."""
    start_time = time.time()  # Start timing

    total_lines = count_lines(file_path)
    midpoint = total_lines // 2

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file, \
         open(part1_path, 'w', encoding='utf-8') as part1, \
         open(part2_path, 'w', encoding='utf-8') as part2:
        for i, line in enumerate(file):
            if i < midpoint:
                part1.write(line)
            else:
                part2.write(line)

    end_time = time.time()
    duration = end_time - start_time

    # Count lines in the new files
    part1_lines = count_lines(part1_path)
    part2_lines = count_lines(part2_path)

    print(f"Time to complete was {int(duration // 60)} minutes: {int(duration % 60)} seconds")
    print(f"Original line count: {total_lines:,}")
    print(f"{os.path.basename(part1_path)} line count: {part1_lines:,}")
    print(f"{os.path.basename(part2_path)} line count: {part2_lines:,}")

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'rockyou.txt')
part1_path = os.path.join(script_dir, 'rockyou_1.txt')
part2_path = os.path.join(script_dir, 'rockyou_2.txt')

split_file(file_path, part1_path, part2_path)
