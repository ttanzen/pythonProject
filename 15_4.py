import re

regex = (r' description.*')
regex1 = (r'^interface\s(?P<iface>\S+)')

def get_ints_without_description(filename):

    with open (filename) as f:
        result = []
        for line in f:
            match1 = re.search(regex1, line)
            match = re.search(regex, line)
            if match1:
                result1 = match1.group('iface')
                result.append(result1)
            elif match:
                result.remove(result1)

        return result

print(get_ints_without_description('config_r1.txt'))