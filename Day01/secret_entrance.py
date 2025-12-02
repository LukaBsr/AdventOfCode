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
        
        if direction == 'L':
            number = (number - value) % 100
        elif direction == 'R':
            number = (number + value) % 100

        if number == 0:
            zero_count += 1
    
    return number, zero_count

def main():
    result = process_commands("input.txt")

    if result is not None:
        final_number, zero_times = result
        print(f"Final number: {final_number}")
        print(f"Number reached 0: {zero_times} time(s)")

if __name__ == "__main__":
    main()
