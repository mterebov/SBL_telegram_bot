def inforeader(name):
    info_output = ''
    with open(name, encoding='utf8') as f:
        info = f.readlines()
    f.close()
    for line in info:
        info_output += line
    return info_output
