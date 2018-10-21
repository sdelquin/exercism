def right_checksum(clean_isbn):
    v, n = 0, len(clean_isbn)
    for i, digit in enumerate(clean_isbn):
        v += (n - i) * digit
    return (v % 11 == 0)


def clean_isbn(raw_isbn):
    isbn = list(raw_isbn.replace('-', ''))
    if len(isbn) != 10:
        return False
    if isbn[-1] == 'X':
        isbn[-1] = '10'
    try:
        return list(map(int, isbn))
    except ValueError:
        return False


def verify(isbn):
    cleaned_isbn = clean_isbn(isbn)
    return cleaned_isbn and right_checksum(cleaned_isbn)
