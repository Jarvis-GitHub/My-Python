import sys
script, input_encoding, error = sys.argv


def main(language_file, encoing, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoing, errors)
        return main(language_file, encoing, errors)


def print_line(line, encoing, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoing, errors=errors)
    cooked_string = raw_bytes.decode(encoing, errors=errors)

    print(raw_bytes, "<==>", cooked_string)


languages = open("ex23_languages.txt", encoding="utf-8")
main(languages, input_encoding, error)
