import csv

def load_names_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        return {row[0].strip().lower() for row in reader}

class PalindromeChecker:
    def __init__(self, names_set):
        self.names_set = names_set

    def find_palindrome_names(self, username):
        reverse_username = username[::-1].lower()
        if reverse_username in self.names_set:
            return [reverse_username]
        return []

class AnagramChecker:
    def __init__(self, names_set):
        self.names_set = names_set
        self.sorted_names_dict = {name: ''.join(sorted(name.lower())) for name in self.names_set}

    def find_anagram_names(self, username):
        sorted_username = ''.join(sorted(username.lower()))
        return [name for name, sorted_name in self.sorted_names_dict.items() if sorted_username == sorted_name]

def write_matches_to_file(file_name, username, palindromes, anagrams):
    with open(file_name, 'w') as file:
        file.write(f"Matches for '{username}':\n\n")
        file.write("Palindromes:\n")
        for palindrome in palindromes:
            file.write(f"{palindrome}\n")
        file.write("\nAnagrams:\n")
        for anagram in anagrams:
            file.write(f"{anagram}\n")

file_path = 'names_no_duplicates.csv'  # Replace with your file path
names_set = load_names_from_csv(file_path)

palindrome_checker = PalindromeChecker(names_set)
anagram_checker = AnagramChecker(names_set)

username = input("Enter a username (up to 11 characters): ").strip()[:11]

palindromes = palindrome_checker.find_palindrome_names(username)
anagrams = anagram_checker.find_anagram_names(username)

output_file_name = "username_matches.txt"
write_matches_to_file(output_file_name, username, palindromes, anagrams)

print(f"\nMatches for '{username}':")
if palindromes:
    print("Palindromes:")
    for palindrome in palindromes:
        print(f"  '{palindrome}'")
else:
    print("  No palindromes found.")

if anagrams:
    print("Anagrams:")
    for anagram in anagrams:
        print(f"  '{anagram}'")
else:
    print("  No anagrams found.")

print(f"\nMatches have also been written to '{output_file_name}'.")
