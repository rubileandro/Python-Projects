import itertools
import os
from mobile_network_codes import providers_dict


def generate_numbers_for_provider(provider_name):
    prefixes = providers_dict[provider_name]
    for prefix in prefixes:
        for suffix in itertools.product(range(10), repeat=8 - len(str(prefix))):
            yield str(prefix) + ''.join(map(str, suffix))


def save_numbers_to_file(numbers, mode='w'):
    with open('generated_numbers.txt', mode) as file:
        for number in numbers:
            file.write(number + '\n')


def display_stats():
    file_size = os.path.getsize('generated_numbers.txt') / (1024 * 1024)  # Convert size to MB
    with open('generated_numbers.txt', 'r') as file:
        line_count = sum(1 for _ in file)

    print(f"\nFile size: {file_size:.2f} MB")
    print(f"Total numbers generated: {line_count:,}")


def main():
    print("Choose a provider:")
    for index, provider in enumerate(providers_dict.keys()):
        print(f"{index + 1}. {provider}")

    print("4. All Providers")
    choice = input("\nEnter your choice: ")

    if choice == "4":
        for index, provider in enumerate(providers_dict.keys()):
            numbers = generate_numbers_for_provider(provider)
            mode = 'a' if index > 0 else 'w'
            save_numbers_to_file(numbers, mode)
    else:
        provider_name = list(providers_dict.keys())[int(choice) - 1]
        numbers = generate_numbers_for_provider(provider_name)
        save_numbers_to_file(numbers)

    print("Numbers have been generated and saved to generated_numbers.txt")
    display_stats()


if __name__ == "__main__":
    main()
