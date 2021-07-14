
def get_int_vlan_map(config_filename):
    access = {}
    trunk = {}
    with open(config_filename) as f:

        for line in f:
            if 'interface' in line:
                interface = line.split()[1]
            elif 'access vlan' in line:
                a_vlan = line.split()[3]
                access[interface] = {}
                access[interface] = int(a_vlan)
            elif 'allowed vlan' in line:
                t_vlans = (line.split()[4])
                t_vlans = t_vlans.split(',')
                vlans = [int(i) for i in t_vlans]
                trunk[interface] = vlans
    return (access,trunk)

print (get_int_vlan_map('config_sw1.txt'))


