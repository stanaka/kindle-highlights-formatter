import argparse
import re
from datetime import datetime

def parse_clippings(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    clippings = content.split('==========')
    books = {}

    for clipping in clippings:
        clipping = clipping.strip()
        if not clipping:
            continue

        lines = clipping.split('\n')
        title = lines[0].strip()
        meta = lines[1].strip()
        highlight = '\n'.join(lines[2:]).strip()

        if not highlight:
            continue

        date_match = re.search(r'Added on (.+)', meta)
        if not date_match:
            continue
        
        date_str = date_match.group(1).strip()
        # Remove weekday name because locale can be different
        date_str = ', '.join(date_str.split(', ')[1:])
        try:
            last_highlight_time = datetime.strptime(date_str, '%B %d, %Y %I:%M:%S %p')
        except ValueError:
            # Handle cases where the month name is in a different language
            # This is a simple example, a more robust solution would be needed for full localization
            continue

        if title not in books:
            books[title] = {'highlights': [], 'last_highlight_time': None}

        books[title]['highlights'].append({'meta': meta, 'highlight': highlight})
        if books[title]['last_highlight_time'] is None or last_highlight_time > books[title]['last_highlight_time']:
            books[title]['last_highlight_time'] = last_highlight_time

    return books

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default='My Clippings.txt', help='input file')
    parser.add_argument('-t', '--titles', action='store_true', help='display only titles of books')
    parser.add_argument('-b', '--book', type=int, help='only display contents for book NUMBER')
    args = parser.parse_args()

    books = parse_clippings(args.input)
    
    sorted_books = sorted(books.items(), key=lambda item: item[1]['last_highlight_time'], reverse=True)

    if args.titles:
        for i, (title, data) in enumerate(sorted_books):
            last_highlight_time_str = data['last_highlight_time'].strftime('%A, %B %d, %Y %I:%M:%S %p')
            print(f'{i+1}. {title} (Last highlighted: {last_highlight_time_str})')
    elif args.book is not None:
        if 1 <= args.book <= len(sorted_books):
            title, data = sorted_books[args.book - 1]
            last_highlight_time_str = data['last_highlight_time'].strftime('%A, %B %d, %Y %I:%M:%S %p')
            print(f'# {title} (Last highlighted: {last_highlight_time_str})')
            for h in data['highlights']:
                meta_info = h['meta'].replace('- Your Highlight on ', '').split(' | ')[0]
                print(f'- {meta_info}')
                print(f'> {h["highlight"]}')
    else:
        for title, data in sorted_books:
            last_highlight_time_str = data['last_highlight_time'].strftime('%A, %B %d, %Y %I:%M:%S %p')
            print(f'# {title} (Last highlighted: {last_highlight_time_str})')
            for h in data['highlights']:
                meta_info = h['meta'].replace('- Your Highlight on ', '').split(' | ')[0]
                print(f'- {meta_info}')
                print(f'> {h["highlight"]}')

if __name__ == '__main__':
    main()
