def format_number(num, format_char):
    result = format(num, format_char)
    return result

result = format_number(145, 'o')
print(result)