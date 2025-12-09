#!/usr/bin/env python3

def find_max(bank: str) -> int:
    max_joltage = 0
    
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)
    
    return max_joltage

def main():
    with open('input.txt', 'r') as f:
        banks = f.read().strip().split('\n')
    if not banks or banks == ['']:
        print("No banks found in input.txt")
        return 84
    
    total_joltage = 0
    
    for bank in banks:
        max_joltage = find_max(bank)
        total_joltage += max_joltage
    
    print(f"Total output joltage: {total_joltage}")
    return 0

if __name__ == "__main__":
    main()
