import re

regex = (r'ip address (?P<ip>[\d.]+)\s(?P<mask>[\d.]+)')

def get_ip_from_cfg(filename):
    result = []
    with open (filename) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                result.append(match.groups())
        return result

print(get_ip_from_cfg('config_r1.txt'))