
trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_config_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    """
    intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы
  такого вида:
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
    - trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде
  списка команд (список trunk_mode_template)
    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    i = []
    for intf, vlans in intf_vlan_mapping.items():
       i.append (f'''interface {intf}''')
       for command in trunk_template:
           if command.endswith('allowed vlan'):
              i.append(f'''{command} {str(vlans)[1:-1].replace(' ','')}''')
           else:
              i.append(f'''{command}''')

    return i
print(generate_trunk_config(trunk_config, trunk_mode_template))