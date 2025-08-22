def clean_word(word):
    """Remove punctuation from a word and convert to lowercase."""
    cleaned = ""
    for char in word:
        if char.isalpha():
            cleaned += char.lower()
    return cleaned

def count_words(text, stop_words):
    """Count word frequencies excluding stop words."""
    # Split text into words
    words = text.split()
    
    # Dictionary to store word counts
    word_count = {}
    
    # Process each word
    for word in words:
        # Clean the word (remove punctuation, convert to lowercase)
        cleaned_word = clean_word(word)
        
        # Skip empty strings and stop words
        if cleaned_word and cleaned_word not in stop_words:
            if cleaned_word in word_count:
                word_count[cleaned_word] += 1
            else:
                word_count[cleaned_word] = 1
    
    return word_count

def get_top_words(word_count, num_words=5):
    """Get the top N most frequent words."""
    # Convert dictionary to list of tuples (word, count)
    word_list = []
    for word, count in word_count.items():
        word_list.append((word, count))
    
    # Sort by count (descending) then by word (ascending) for ties
    # Using bubble sort since students haven't learned advanced sorting
    n = len(word_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Sort by count first (descending), then by word (ascending)
            if (word_list[j][1] < word_list[j + 1][1] or 
                (word_list[j][1] == word_list[j + 1][1] and word_list[j][0] > word_list[j + 1][0])):
                word_list[j], word_list[j + 1] = word_list[j + 1], word_list[j]
    
    # Return top num_words
    return word_list[:num_words]

def main():
    """Main function to run the word frequency analyzer."""
    # Get input from user
    text = input("Enter your text:\n")
    
    stop_words_input = input("Enter stop-words (separated by spaces):\n")
    
    # Convert stop words to lowercase and store in a list
    stop_words = []
    if stop_words_input.strip():  # Check if user entered any stop words
        for word in stop_words_input.split():
            stop_words.append(word.lower())
    
    # Count word frequencies
    word_count = count_words(text, stop_words)
    
    # Get top 5 most frequent words
    top_words = get_top_words(word_count, 5)
    
    # Display results
    print("\nTop 5 most frequent words:")
    for word, count in top_words:
        print(f"{word}: {count}")

# Run the program
if __name__ == "__main__":
    main()