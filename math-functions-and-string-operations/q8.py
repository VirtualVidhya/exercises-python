def validate_dna_sequence(sequence):
    """
    Validates if the input sequence contains only valid DNA nucleotides.
    
    Args:
        sequence (str): DNA sequence to validate
        
    Returns:
        bool: True if sequence is valid, False otherwise
    """
    valid_nucleotides = {'A', 'T', 'C', 'G'}
    return all(nucleotide in valid_nucleotides for nucleotide in sequence.upper())


def convert_dna_to_mrna(dna_sequence):
    """
    Converts DNA sequence to mRNA by applying transcription rules.
    
    Args:
        dna_sequence (str): Valid DNA sequence
        
    Returns:
        str: Corresponding mRNA sequence
    """
    # DNA to mRNA conversion mapping
    conversion_map = {
        'T': 'A',
        'A': 'U', 
        'C': 'G',
        'G': 'C'
    }
    
    return ''.join(conversion_map[nucleotide] for nucleotide in dna_sequence.upper())


def get_valid_dna_input():
    """
    Prompts user for DNA sequence input until a valid sequence is entered.
    
    Returns:
        str: Valid DNA sequence in uppercase
    """
    while True:
        dna_input = input("Enter a DNA sequence: ").strip()
        
        if not dna_input:
            print("Please enter a non-empty DNA sequence.")
            continue
            
        if validate_dna_sequence(dna_input):
            return dna_input.upper()
        else:
            print("Invalid DNA sequence! Please use only A, T, C and G.")


def main():
    """
    Main function that orchestrates the DNA to mRNA conversion process.
    """
    print("DNA to mRNA Converter")
    print("=" * 20)
    
    try:
        # Get valid DNA input from user
        dna_sequence = get_valid_dna_input()
        
        # Convert to mRNA
        mrna_sequence = convert_dna_to_mrna(dna_sequence)
        
        # Display result
        print(f"Converted mRNA: {mrna_sequence}")
        
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()