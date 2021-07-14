with open('CAM_table.txt') as f:
  for line in f:
    if line.startswith(' ') and line[1].isdigit():
      l1 = line.strip().split('   ')
      vlan, mac, interface = l1[0], l1[1].strip(), l1[3]
      print(f'''{vlan:9}{mac:<20}{interface}''')