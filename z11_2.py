from z1_1 import parse_cdp_neighbors

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

def create_network_map(filenames):
    file = []
    for i in filenames:
        with open(i) as f:
            file.append(f.read())

    dct = parse_cdp_neighbors('\n'.join(file))
    return dct

if __name__ == "__main__":
    print(create_network_map(infiles))