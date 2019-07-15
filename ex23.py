import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)   #这个会一直执行，直到line为空时才停止


def print_line(line, encoding, errors):
    next_lang = line.strip()
    '''完完整整就是一个字符串,用来移除字符串头尾指定的字符（默认为空格或者换行符）或字符序列'''
    raw_bytes = next_lang.encode(encoding, errors=errors)
    #调用encode来进行编码
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    #解码，利用decode()来得到我们人类看得懂的语言

    print(raw_bytes, '<===>', cooked_string)


languages = open("languages.txt", encoding='utf-8')

main(languages, encoding, error)
