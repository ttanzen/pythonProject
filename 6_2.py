ip = input('Enter IP-address in x.x.x.x format: ')
first_oct = ip.split('.')[0]
if 0 < int(first_oct) < 224:
    print('unicast')
elif 223 < int(first_oct) < 240:
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')