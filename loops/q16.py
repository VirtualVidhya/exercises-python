def main():
    num_batsmen = int(input("Enter number of batsmen in the squad: "))
    balls_per_batsman = int(input("Enter number of balls faced by each batsman: "))

    print("\n--- Squad Strike-Rate Report ---\n")

    for b in range(1, num_batsmen + 1):
        total_runs = 0

        for ball in range(1, balls_per_batsman + 1):
            runs = int(input(f"Runs scored by batsman-{b} on ball {ball}: "))
            total_runs += runs

        strike_rate = (total_runs / balls_per_batsman) * 100

        print(f"\nBatsman-{b}: Total Runs: {total_runs}, Strike Rate: {strike_rate:.2f}%\n")

if __name__ == "__main__":
    main()
