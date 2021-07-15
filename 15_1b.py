import re

regex = (r'ip address (?P<ip>[\d.]+)\s(?P<mask>[\d.]+)')
regex1 = (r'^interface\s(?P<iface>\S+)')

def get_ip_from_cfg(filename):

    with open (filename) as f:
        result = {}

        for line in f:
            match1 = re.search(regex1, line)
            match = re.search(regex, line)
            if match1:
                result1 = match1.group('iface')
                addresses = []
            elif match:
                addresses.append(match.groups())
                result[result1] = addresses
    return result

print(get_ip_from_cfg('config_r2.txt'))