import re

regex = (r'^(\S+) +(\S+) +\w+\s\w+\s+(\w+\s*?\w*) +(\w+$)')

def parse_sh_ip_int_br(filename):
    result = []
    with open (filename) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                result.append(match.groups())
        return result


print (parse_sh_ip_int_br('sh_ip_int_br.txt'))