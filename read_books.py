# Open and Read a File (Session 9&10 - Files)
def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:  # Using with open() (Session 11&12 - Best Practices)
            text = file.read()
        return text
    except FileNotFoundError:  # Handling file errors (Session 5&6 - Exception Handling)
        print(f"Error: File '{filename}' not found.")
        return ""


# Process Text to Find Unique Words Using a Dictionary (Session 11&12 - Dictionaries)
def count_unique_words(text):
    text = text.lower()  # Convert text to lowercase (Session 7&8 - String Methods)
    punctuation = ".,!?;:()[]{}\"'“”"  # Define characters to remove (Session 7&8 - String Operations)

    for p in punctuation:
        text = text.replace(p, " ")  # Remove punctuation

    words = text.split()  # Split text into words (Session 7&8 - String Methods)

    word_dict = {}  # Using dictionary to track words (Session 11&12 - Dictionaries)
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1  # Counting words efficiently

    return len(word_dict)  # Number of unique words (length of dictionary)


# Compare Two Books Using Tuples (Session 11&12 - Tuples)
def compare_books(file1, file2):
    text1 = read_file(file1)
    text2 = read_file(file2)

    unique_count1 = count_unique_words(text1)
    unique_count2 = count_unique_words(text2)

    print(f"Unique words in {file1}: {unique_count1}")
    print(f"Unique words in {file2}: {unique_count2}")

    # Store results in tuples (Session 11&12 - Tuples)
    result = (file1, unique_count1), (file2, unique_count2)

    # Compare the books (Session 5&6 - Conditional Execution)
    if unique_count1 > unique_count2:
        print(f"{result[0][0]} has more unique words!")
    elif unique_count2 > unique_count1:
        print(f"{result[1][0]} has more unique words!")
    else:
        print("Both books have the same number of unique words.")


# Example usage (Replace with actual book file names)
book1 = "Frankenstein.txt"
book2 = "Wonderland.txt"

compare_books(book1, book2)
