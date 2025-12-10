#!/usr/bin/env python3

def parse_input(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
    
    parts = content.split('\n\n')
    ranges = []
    available_ids = []

    for line in parts[0].split('\n'):
        start, end = line.split('-')
        ranges.append((int(start), int(end)))
    
    for line in parts[1].split('\n'):
        available_ids.append(int(line))
    
    return ranges, available_ids

def is_fresh(ingredient_id, ranges):
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False

def main():
    ranges, available_ids = parse_input('input.txt')
    count = 0
    
    for ingredient_id in available_ids:
        if is_fresh(ingredient_id, ranges):
            count += 1
    
    print(f"Final result: {count}")
    return count

if __name__ == "__main__":
    main()