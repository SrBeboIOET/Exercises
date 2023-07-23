import os

def get_name():
    name_file = input("Enter the name of file: \n")
    return name_file

def print_file_name(name_file):
    print("The name of file is:", name_file)

def print_file_path(name_file):
    file_path = os.path.abspath(name_file)
    print("The path of file is:", file_path)

def count_word_frequency(name_file):
    try:
        with open(name_file, "r") as file:
            content = file.read()
            words = content.split()
            frequency = {}

            for word in words:
                frequency[word] = frequency.get(word, 0) + 1

            for word in sorted(frequency):
                print(word, "---", frequency[word])
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    name_file = get_name()
    print_file_name(name_file)
    print_file_path(name_file)
    count_word_frequency(name_file)
