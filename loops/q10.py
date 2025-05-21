def main():
    board_size = int(input("Enter board size (even number): "))
        
    # Generate and print the checkerboard
    for i in range(board_size):
        row = []
        for j in range(board_size):
            # On even (i+j) positions place 'X', on odd positions place 'O'
            row.append('X' if (i + j) % 2 == 0 else 'O')
        print(' '.join(row))

if __name__ == "__main__":
    main()