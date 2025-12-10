#!/usr/bin/env python3

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def process_commands(filename):
    content = read_file(filename)
    if content is None:
        return None
    
    number = 50
    zero_count = 0
    lines = content.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        direction = line[0]
        value = int(line[1:])
        
        for _ in range(value):
            if direction == 'L':
                number = (number - 1) % 100
            elif direction == 'R':
                number = (number + 1) % 100
            
            if number == 0:
                zero_count += 1
    
    return zero_count

def main():
    count = process_commands("input.txt")

    print(f"Final count: {count} time(s)")

if __name__ == "__main__":
    main()
