def to_list(csvs:str, seperator:chr=',') -> list:
    output_list = []
    input = csvs.strip()
    if input:
        output_list = [value.strip() for value in csvs.strip().split(seperator)]
    return output_list


def to_int_list(line, seperator:chr=','):
    #return list(map(int, line.split(seperator)))
    return list(map(int, to_list(line, seperator)))