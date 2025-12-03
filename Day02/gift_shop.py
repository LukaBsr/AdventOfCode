#!/usr/bin/env python3

def read_file(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None

def expand_ranges(text):
    if not text:
        return
    for token in text.replace('\n', '').split(','):
        t = token.strip()
        if not t:
            continue
        if '-' in t:
            a, b = t.split('-', 1)
            start = int(a)
            end = int(b)
            if start > end:
                start, end = end, start
            for i in range(start, end + 1):
                yield i
        else:
            yield int(t)

def is_double_repeat(n):
    s = str(n)
    if s.startswith('-'):
        return False
    if len(s) % 2:
        return False
    h = len(s) // 2
    return s[:h] == s[h:]

def main():
    content = read_file('input.txt')
    if content is None:
        print('input.txt not found')
        return

    invalids = []
    for id_ in expand_ranges(content):
        if is_double_repeat(id_):
            invalids.append(id_)

    total = sum(invalids)
    print(total)

if __name__ == '__main__':
    main()
