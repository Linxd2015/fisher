def is_isbn_or_key(word):
    # isbn13:13个0-9的数字组成
    # isbn10:10ge0-9数字组成，还包含'-'
    isbn_or_key = 'key'
    # 判断q是不是13位且全是数字
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    # 将‘-’全部替换掉，判断是不是10位且全是数字
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key