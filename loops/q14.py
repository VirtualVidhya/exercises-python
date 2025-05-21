def main():
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))

    # Top border
    print(' '.join(['*'] * width))

    # Middle rows
    for _ in range(height - 2):
        # One '*' at each end, with spaces in between
        # inner_spaces = 
        inner_spaces = ' ' * (2 * width - 4)
        print('* ' + inner_spaces + '*')

    # Bottom border (only if height > 1)
    if height > 1:
        print(' '.join(['*'] * width))

if __name__ == "__main__":
    main()