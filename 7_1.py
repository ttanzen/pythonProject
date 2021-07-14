with open('ospf.txt') as f:
    l1 = f.readline().strip().split(' ')
    prefix, metric, nexthop, update, interface = l1[-6], l1[-5].strip('[]'), l1[-3].rstrip(','), l1[-2].rstrip(','), l1[-1]
    print(f'''
    {'Prefix':22} {prefix:20}
    {'AD/Metric':22} {metric:20}
    {'Next-Hop':22} {nexthop:20}
    {'Last update':22} {update:20}
    {'Outbound Interface':22} {interface:20}
    ''')