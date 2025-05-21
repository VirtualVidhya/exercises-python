def hcf(a, b):      # gcd
    mx = max(a, b)

    while True:
        if mx % a == 0 and mx % b == 0:
            return mx
        mx -= 1

    # while b:
    #     a, b = b, a % b
    # return a

def lcm(a, b):
    mx = max(a, b)

    while True:
        if mx % a == 0 and mx % b == 0:
            return mx
        mx += 1

def main():
    x = int(input("Enter apple delivery interval (days): "))
    A = int(input("Enter apple crates per delivery: "))
    y = int(input("Enter orange delivery interval (days): "))
    B = int(input("Enter orange crates per delivery: "))

    max_per_basket = hcf(A, B)

    # next_full_pack = (x * y) // gcd(x, y)
    next_full_pack = lcm(x, y)

    print(f"\nMaximum crates per basket: {max_per_basket}")
    print(f"Next matching delivery in: {next_full_pack} days")

if __name__ == "__main__":
    main()
