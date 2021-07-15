import re
def convert_ios_nat_to_asa(src_file, dst_file):
    regex = (r'ip nat inside source static tcp (?P<ip>[\d.]+)\s(?P<port1>\d+) interface \S+\s(?P<port2>\d+)')
    with open(src_file) as src, open(dst_file, 'w+') as dest:
        for line in src:
            match = re.search(regex, line)
            if match:
                dest.write(
f'''{'object network LOCAL_'}{match.group('ip')}
{' host'} {match.group('ip')}
{' nat (inside,outside) static interface service tcp'} {match.group('port1')} {match.group('port2')}
''')