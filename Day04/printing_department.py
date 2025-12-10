#!/usr/bin/env python3

def count_rolls(grid, row, col):
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            
            nr, nc = row + dr, col + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == '@':
                    count += 1
    
    return count

def solve():
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    
    grid = [list(line) for line in lines]
    count = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                rolls = count_rolls(grid, row, col)
                
                if rolls < 4:
                    count += 1
    
    print(f"Final result: {count}")
    return count

if __name__ == "__main__":
    solve()
