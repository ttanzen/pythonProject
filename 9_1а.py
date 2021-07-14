
access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}


def generate_access_config(intf_vlan_mapping, access_template, psecurity=None ):
    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access
    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    i = []
    for intf, vlan in intf_vlan_mapping.items():
       i.append (f'interface {intf}')
       for command in access_template:
           if command.endswith('access vlan'):
              i.append(f'{command} {vlan}')
           else:
              i.append(f'{command}')
       for command2 in port_security_template:
           if psecurity:
              i.append(f'{command2}')
    return i

#print(generate_access_config(access_config, access_mode_template))
print(generate_access_config(access_config, access_mode_template, port_security_template))