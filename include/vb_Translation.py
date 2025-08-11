def left(string: str, len):
    return string[0:len]

def split(string: str, separator: str):
    return string.split(separator)

def join(list: list, delim: str):
     return delim.join(list)

def writeline(file, text: str):
    file.write(text)
    file.write("\n")

def mid(string, start, len=None):
    if len:
        return string[start-1:len]
    else:
        return string[start-1:]