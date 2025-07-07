import string


def get_text_input():
    """Get text input from user."""
    print("Enter your text:")
    text = input().strip()
    return text


def get_stop_words():
    """Get stop words from user input."""
    stop_words_input = input("Enter stop-words (separated by spaces): ").strip()
    stop_words = set(word.lower() for word in stop_words_input.split())
    return stop_words


def extract_words(text):
    """Extract words from text, removing punctuation and converting to lowercase."""
    # Remove punctuation and convert to lowercase
    text_clean = text.lower()
    
    # Replace punctuation with spaces
    for punct in string.punctuation:
        text_clean = text_clean.replace(punct, ' ')
    
    # Split into words and filter out empty strings
    words = [word for word in text_clean.split() if word]
    return words


def filter_stop_words(words, stop_words):
    """Filter out stop words from the word list."""
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words


def get_top_words(words, top_n=5):
    """Get the top N most frequent words using dictionary counting."""
    # Count word frequencies manually using a dictionary
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Convert dictionary to list of tuples and sort by count (descending)
    word_list = [(word, count) for word, count in word_counts.items()]
    word_list.sort(key=lambda x: x[1], reverse=True)
    
    # Return top N words
    return word_list[:top_n]


def display_results(top_words):
    """Display the word frequency results."""
    print()
    for word, count in top_words:
        print(f"{word}: {count}")


def main():
    """Main function to orchestrate the word frequency analysis."""
    # Get user input
    text = get_text_input()
    stop_words = get_stop_words()
    
    # Extract words from text
    words = extract_words(text)
    
    # Filter out stop words
    filtered_words = filter_stop_words(words, stop_words)
    
    # Get top 5 most frequent words
    top_words = get_top_words(filtered_words, 5)
    
    # Display results
    display_results(top_words)


if __name__ == "__main__":
    main()