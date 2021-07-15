import re
import csv

def write_dhcp_snooping_to_csv(filenames, output):
  data = ['switch', 'mac', 'ip', 'vlan', 'interface']
  regex = re.compile(r'(?P<mac>\S+) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<port>\S+)')
  result = []
  for file in filenames:
    host = file.split('_')[0]
    with open (file) as f:
        for match in regex.finditer(f.read()):
            mac, ip, vlan, port = match.groups()
            result.append([host, mac, ip, vlan, port])
  result.insert(0, data)
  print(result)
  with open(output, 'w+') as dest:
    writer = csv.writer(dest)
    writer.writerows(result)


if __name__ == "__main__":
    files = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
    write_dhcp_snooping_to_csv(files, 'result.csv')