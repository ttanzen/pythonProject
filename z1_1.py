def parse_cdp_neighbors(command_output):
    dct = {}
#    l = command_output.strip().split('\n')

    for line in command_output.strip().split('\n'):
        columns = line.split()
        if ">" in line:
            d1 = line.split('>')[0]

        if len(columns) >= 5 and columns[3].isdigit():
           r_d, l_int, l_int_num, *other, r_int, r_int_num = columns
           dct[(d1, l_int + l_int_num)] = (r_d, r_int + r_int_num)

    return  dct

if __name__ == "__main__":
    with open("sh_cdp_n_r3.txt") as f:
        print(parse_cdp_neighbors(f.read()))