import re


regex = (r'(?P<host>\w+\d+)\s+(?P<l_i>\w+\s\S+)\s+\d+\s+[\w ]+\s+\S+\s+(?P<r_i>\w+\s\S+)')

def generate_description_from_cdp(filename):

    with open (filename) as f:
        result = {}
        for m in re.finditer(regex, f.read()):
            result[m.group('l_i')] = f'''description Connected to {m.group('host')} port {m.group('r_i')}'''
        return result

if __name__=="__main__":
    print(generate_description_from_cdp('sh_cdp_n_sw1.txt'))