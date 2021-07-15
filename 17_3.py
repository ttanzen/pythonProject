import re

def parse_sh_cdp_neighbors(command_output):
   regex = ('(?P<local_host>\w+)>show cdp neighbors')
   regex1 = ('(?P<host>\w+\d+)\s+(?P<l_i>\w+\s\S+)\s+\d+\s+[\w ]+\s+\S+\s+(?P<r_i>\w+\s\S+)')
   result = {}
   local_host = re.search(regex, command_output).group('local_host')
   result[local_host] = {}
   for m in re.finditer(regex1, command_output):
                result[local_host][m.group('l_i')] = {m.group('host') : m.group('r_i')}
   return result

if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_sh_cdp_neighbors(f.read()))