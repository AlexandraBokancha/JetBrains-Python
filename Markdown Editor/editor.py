formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line', 'ordered-list', 'unordered-list']
special_commands = ['!help', '!done']
save_output = []
possible_levels = [1, 2, 3, 4, 5, 6]


def headings():
    while True:
        level = int(input('Level: '))
        if level not in possible_levels:
            print('The level should be within the range of 1 to 6')
        else:
            break
    text = input('Text: ')
    return f'{level * "#"} {text}\n'


bold = lambda text: f'**{text}**'
italic = lambda text: f'*{text}*'
plain = lambda text: text
inline_code = lambda text: f'`{text}`'

format_functions = {
    'plain': plain,
    'bold': bold,
    'italic': italic,
    'inline-code': inline_code,
}

def link():
    label = input('Label: ')
    url = input('URL: ')
    return f'[{label}]({url})'


def lists():
    rows = []
    while True:
        number_of_rows = int(input('Number of rows: '))
        if number_of_rows <= 0:
            print('The number of rows should be greater than zero')
            continue
        else:
            for n in range(number_of_rows):
                n += 1
                print(f'Row #{n}: ', end='')
                row = input()
                rows.append(row)
        break
    return rows


while True:
    possible_format = input('Choose a formatter: ')
    if possible_format == '!done':
        with open('output.md', 'w') as f:
            for element in save_output:
                f.write(element)
        break
    elif possible_format not in formatters:
        print('Unknown formatting type or command')
    else:
        if possible_format == 'ordered-list':
            for order_num, x in enumerate(lists()):
                save_output.append(f'{order_num+1}. {x}\n')
        elif possible_format == 'unordered-list':
            for x in lists():
                save_output.append(f'* {x}\n')
        elif possible_format == 'link':
            save_output.append(link())
        elif possible_format == 'header':
            save_output.append(headings())
        elif possible_format == 'new-line':
            save_output.append('\n')
        else:
            text = input('Text: ')
            function = format_functions[possible_format]
            result = function(text)
            save_output.append(result)
        if len(save_output) != 0:
            print("".join(save_output))


