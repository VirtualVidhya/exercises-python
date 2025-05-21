def main():
    n = int(input("Enter the number of bands: "))
    
    total_lineups = 1
    
    for i in range(2, n + 1):
        total_lineups *= i
    
    print(f"Total possible lineups: {total_lineups}")

if __name__ == "__main__":
    main()
