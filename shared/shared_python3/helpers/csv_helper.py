def to_int_list(line, seperator:chr=','):
    return list(map(int, line.split(seperator)))


def to_list(csvs:str) -> list:
    output_list = []
    input = csvs.strip()
    if input:
        output_list = [value.strip() for value in csvs.strip().split(',')]
    return output_list