vl = input('Enter vlan id please: ')
res = []
with open('CAM_table.txt') as f:
  for line in f:
    if line.startswith(' ') and line[1].isdigit():
      l1 = line.strip().split('   ')
      vlan, mac, interface = int(l1[0]), l1[1].strip(), l1[3].strip()
      line = [int(vlan), mac, interface]
      res.append(line)

for vlan, mac, interface in sorted(res):
    if vlan == int(vl):
      print (f'''{vlan:<9}{mac:<20}{interface}''')